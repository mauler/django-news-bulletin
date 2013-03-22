#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin

from .models import Rss, Bulletin, Entry


admin.site.register(Rss)


class BulletinAdmin(admin.ModelAdmin):
    filter_horizontal = ("entries", )


admin.site.register(Bulletin, BulletinAdmin)


admin.site.register(Entry)
