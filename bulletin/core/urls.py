#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^(?P<bulletin_pk>\d+)/$', 'bulletin', name='bulletin'),
)
