# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import TalkView


urlpatterns = patterns('',
    url('^(?:(?P<slug>[^/]+))?$', TalkView.as_view(), name="talk"),
)
