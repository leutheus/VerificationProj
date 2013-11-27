from django.conf.urls import patterns, include, url
from userauth import views

urlpatterns = patterns('',
    url(r'^anmelden/$', 'django.contrib.auth.views.login', {'template_name': 'userauth/login.html'},
        name='userauth_login'),

    url(r'^abmelden/$', 'django.contrib.auth.views.logout', {'next_page': '/vcloud/'},
        name='userauth_logout'),

       url(r'^passwort-aendern/$', 'django.contrib.auth.views.password_change', 
        {'template_name': 'userauth/password_change_form.html', 'post_change_redirect': '/password_change_done'}, 
        name='userauth_password_change'),

    url(r'^passwort-geaendert/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'userauth/password_change_done.html'},
        name='userauth_password_change_done')
)
