# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PageView


urlpatterns = patterns('',
    url('^(?P<slug>[^/]+)/$', PageView.as_view(), name="page"),
)
