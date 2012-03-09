# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jssettings/$', 'django.views.generic.simple.direct_to_template', {'template': 'jssettings.js', 'mimetype': 'application/x-javascript', 'extra_context': {'settings':settings}}, name="jssettings"),
    url(r'^pages/', include('newmediology.pages.urls')),
    url(r'^', include('newmediology.conversation.urls')),
)
