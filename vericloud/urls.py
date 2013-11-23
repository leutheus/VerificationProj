from django.conf.urls import patterns, include, url

from vericloud import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),

	url(r'^addMark/$', views.addMark, name='addMark'),
)