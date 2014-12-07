import os
import re
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from documents.models import Article, Title, SubTitle, Content, Keyword
from documents.forms import UploadFileForm

# Create your views here.
def listArticle(request):
    articleList = Article.objects.all()
    content = {'articleList': articleList}
    return render(request, 'documents/listArticle.html', content)

def detail(request, articleID):
    article = get_object_or_404(Article, id=articleID)
    content = {'articleName': article.name}
    return render(request, 'documents/listContent.html', content)

@csrf_exempt
def upload(request):
    '''
    if request.method == 'POST':
        fileName = request.POST['fileName']
        myPath = os.path.join('input', fileName)
        upload = Article(name=fileName, path=myPath)
        upload.save()

        form = UploadFileForm(request.POST, request.FILES)
        if True:
            filePath = os.path.join(settings.BASE_DIR, '..', myPath)
            serverFile = open(filePath, 'wb+')
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)
            sererFile.close()

            parseInputDocument(1)
            return HttpResponseRedirect(reverse('documents:listArticle')) 

        else:
            return HttpResponse("fail")

    else:
        return HttpResponse("not post")
    '''

def parseInputDocument(articleID):
    def preProcessing(line):
        line = re.sub('\\\\\\\\', '__MY_BACKSLASH__', line)
        line = re.sub('\\\\\*', '__MY_START__', line)
        line = line.lstrip(' ').rstrip('\n')
        return line

    def restore(string):
        string = re.sub('__MY_BACKSLASH__', '\\\\', string)
        string = re.sub('__MY_START__', '*', string)
        return string

    def saveKeyword(keywords, newContent):
        i = 0
        for m in keywords:
            st = m.start(0) - 4*i - 2
            l = m.end(0) - m.start(0) - 4
            newKeyword = Keyword(startPos=st, length=l, contentID=newContent)
            newKeyword.save()

    article = get_object_or_404(Article, id=articleID)
    filePath = os.path.join(settings.BASE_DIR, '..', article.path)
    f = open(filePath)
    newTitle = Title()
    newSubTitle = SubTitle()
    newContent = Content()

    while True:
        line = f.readline()
        if not line: break

        line = preProcessing(line)
        if not line: continue

        if line[0] == '#':
            text = line.lstrip('#')
            newTitle = Title(titleText=restore(text), articleID=article)
            newTitle.save()

        elif line[0] >= '0' and line[0] <= '9':
            isImp = False
            text = re.sub('\d+. ', '', line)
            if text:
                if text[0] == '*':
                    text = text[2:len(text)-2]
                    isImp = True

                newSubTitle = SubTitle(subTitleText=text, titleID=newTitle, isImportant=isImp)
                newSubTitle.save()

        else:
            keywords = re.finditer('\*\*.*?\*\*', line)
            text = re.sub('\*\*', '', line)

            text = restore(text)
            isImp = line[0] == '*'

            text = text[2:len(text)]
            newContent = Content(content=text, subTitleID=newSubTitle, isImportant=isImp)
            newContent.save()

            saveKeyword(keywords, newContent)

    f.close()


