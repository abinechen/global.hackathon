from django.conf.urls import patterns, url
 
from documents import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^listArticle/$', views.listArticle, name='listArticle'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
