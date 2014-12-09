from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from documents import views
from django.conf import settings
import django.contrib.staticfiles

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^listArticle/$', views.listArticle, name='listArticle'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^puzzle/$', views.puzzle, name='puzzle'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^game/$', views.game, name='game'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)

urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes': True}),
    )