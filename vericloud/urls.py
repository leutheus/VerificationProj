from django.conf.urls import patterns, include, url

from vericloud import views

urlpatterns = patterns('',
	
	url(r'^addMark/$', views.addMark, name='addMark'),
	url(r'^addFile/$', views.addFile, name='addFile'),
	url(r'^newFile/$', views.newFile, name="'newFile"),
	url(r'^listFiles/$', views.listFiles, name="listFiles"),
	url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),
	url(r'^$', views.index, name='index'),
)