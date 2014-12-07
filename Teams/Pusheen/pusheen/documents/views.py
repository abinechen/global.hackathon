from django.shortcuts import render

from documents.models import Article

# Create your views here.
def listArticle(request):
    articleList = Article.objects.all()
    content = {'articleList': articleList}
    return render(request, 'documents/listArticle.html', content)

