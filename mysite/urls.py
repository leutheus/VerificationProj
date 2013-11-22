from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^benutzer/', include('userauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
