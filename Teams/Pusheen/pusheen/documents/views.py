from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from documents.models import Article, Title, SubTitle, Content, Keyword

from .forms import UploadFileForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


from django.core.urlresolvers import reverse
import os
import re
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.utils import encoding

# Create your views here.
def index(request):
    context = {'a': 'A', 'b':'B'}
    return render(request, 'documents/index.html', context)

def listArticle(request):
    articleList = Article.objects.all()
    content = {'articleList': articleList}
    return render(request, 'documents/listArticle.html', content)

def handle_uploaded_file(f, path):
    try:
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except:
        raise TypeError("ZZZZZZZ2")

def listing(request):
    titles = get_Titles()
    subtitles = get_SubTitles()
    contents = get_Content()
    keywords = get_Keyword()
    context = {'titles': titles, 'subtitles': subtitles, 'contents': contents, 'keywords': keywords}
    return render(request, 'documents/listing.html', context)

def get_Titles():
    titles = Title.objects.all()
    return titles

def get_SubTitles():
    subtitles = SubTitle.objects.all()
    return subtitles
    
def get_Content():
    contents = Content.objects.all()
    return contents

def get_Keyword():
    keywords = Keyword.objects.all()
    return keywords

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        fileName = request.POST['fileName']
        myPath = os.path.join('input', fileName)
        upload = Article(name=fileName, path=myPath)
        upload.save()

        filePath = os.path.join(settings.BASE_DIR, '..', myPath)
        form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['file'], filePath)
        parseInputDocument(upload.id)
        return HttpResponseRedirect('/documents/listArticle/')
    else:
        form = UploadFileForm()

def parseInputDocument(articleID):
    def preProcessing(line):
        line = re.sub('\\\\\\\\', '__MY_BACKSLASH__', line)
        line = re.sub('\\\\\*', '__MY_START__', line)
        line = line.lstrip(' ').rstrip('\n').rstrip('\r')
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

                newSubTitle = SubTitle(subTitleText=convert_unicode_to_string(text), titleID=newTitle, isImportant=isImp)
                newSubTitle.save()

        else:
            keywords = re.finditer('\*\*.*?\*\*', line)
            text = re.sub('\*\*', '', line)

            text = restore(text)
            isImp = line[0] == '*'

            text = text[2:len(text)]
            newContent = Content(content=convert_unicode_to_string(text), subTitleID=newSubTitle, isImportant=isImp)
            newContent.save()

            saveKeyword(keywords, newContent)

    f.close()

def convert_unicode_to_string(x):
    """
    >>> convert_unicode_to_string(u'ni\xf1era')
    'niera'
    """
    return encoding.smart_str(x, encoding='ascii', errors='ignore')
