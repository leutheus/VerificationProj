from django.conf.urls import patterns, include, url

from vericloud import views

urlpatterns = patterns('',
    url(r'^addMark/$', views.addMark, name='addMark'),
    url(r'^addFile/$', views.addFile, name='addFile'),
    url(r'^newFile/$', views.newFile, name="'newFile"),
    url(r'^listFiles/$', views.listFiles, name="listFiles"),
    url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),
    url(r'^results/(?P<run_id>[\w+]*)/$', views.runresult, name="runresult"),
    url(r'^files/(?P<hash>[\w+]*)/$', views.file, name="file"),
    url(r'^filehierarchy/(?P<file_hierarchy_id>[-\w+]*)/$', views.filehierarchy, name="filehierarchy"),
    url(r'^$', views.index, name='index'),
)