from django.conf.urls import patterns, url

from documents import views

urlpatterns = patterns('',
    url(r'^$', views.listArticle, name='listArticle'),
)

