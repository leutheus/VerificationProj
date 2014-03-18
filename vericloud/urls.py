from django.conf.urls import patterns, include, url

from vericloud import views

urlpatterns = patterns('',
    url(r'^addMark/$', views.addmark, name='addmark'),
    url(r'^testfile/$', views.addfile, name="'addfile"),
    url(r'^listFiles/$', views.listfiles, name="listfiles"),
    url(r'^requirements/$', views.listreq, name="listreq"),
    url(r'^limitations/$', views.listlim, name="listlim"),
    url(r'^createrun/$', views.createrun, name="createrun"),
    url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),
    url(r'^results/(?P<run_id>[\w+]*)/$', views.runresult, name="runresult"),
    url(r'^files/(?P<hashvalue>[\w+]*)/$', views.file, name="file"),
    url(r'^filehierarchy/(?P<file_hierarchy_id>[-\w+]*)/$', views.filehierarchy, name="filehierarchy"),
    url(r'^$', views.index, name='index'),
)