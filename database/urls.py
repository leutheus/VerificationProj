from django.conf.urls import patterns, url

from database import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/$',  views.search, name='search'),
    url(r'^searchFile/$', views.searchFile, name='searchFile'),
    url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),
    url(r'^searchFile/(?P<file_name>[\w+]*.c)/$', views.file, name='file')
    
)