from django.conf.urls import patterns, url

from database import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<benchmark_user>[\w+]*)/$', views.detail, name='detail'),

)