from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from documents.models import Article, Title, SubTitle, Content, Keyword

from .forms import UploadFileForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404

# Create your views here.
def index(request):
    #text1 = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']
    #text2 = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
    context = {'a': 'A', 'b':'B'}
    return render(request, 'documents/index.html', context)

def listArticle(request):
    articleList = Article.objects.all()
    content = {'articleList': articleList}
    return render(request, 'documents/listArticle.html', content)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #form = StatementForm(request.POST)
        if True:
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/documents/listArticle/')
        else:
            raise TypeError(str(request.POST))
    else:
        form = UploadFileForm()
    #return render_to_response('upload.html', {'form': form})

def handle_uploaded_file(f):
    try:
        with open('../input/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except:
        raise TypeError("ZZZZZZZ2")
def listing(request):
    latest_title_list = ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']
    latest_subtitle_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
    titles = get_Titles()
    subtitles = get_SubTitles()
    contents = get_Content()
    keywords = get_Keyword()
    context = {'titles': titles, 'subtitles': subtitles, 'contents': contents, 'keywords': keywords}
    return render(request, 'documents/listing.html', context)
    #return HttpResponse("Hello, world. You're at the poll index.")

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