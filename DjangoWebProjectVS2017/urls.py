"""
Definition of urls for DjangoWebProjectVS2017.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
import app.models

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^user/', app.views.user_new, name='user'),
    url(r'^users/', app.views.users_detail, name='users_detail'),
    url(r'^chart/(?P<question_id>\d+)/$', app.views.chart, name='chart'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/add/', app.views.question_new, name='add'),
    url(r'^polls/choice_add/(?P<question_id>\d+)/$', app.views.choice_add, name='choice_add'),
    url(r'^(?P<question_id>\d+)/results/$', app.views.results, name='results'),
    url(r'^polls/(?P<question_id>\d+)/$', app.views.detail, name='detail'),
    url(r'^polls/(?P<question_id>\d+)/vote/$', app.views.vote, name='vote'),
    url(r'^polls/', app.views.index, name='index'),
   
]