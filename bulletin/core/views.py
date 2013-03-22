#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Bulletin


def bulletin(request, bulletin_pk):
    obj = get_object_or_404(Bulletin, pk=bulletin_pk)
    html = obj.render()
    return HttpResponse(html)
