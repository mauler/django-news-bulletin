#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase

from .models import Rss, Bulletin


class CoreTest(TestCase):

    def test_entries(self):
        rss = Rss(url='http://tvg.globo.com/novelas/malhacao/2012/rss/')
        rss.save()
        self.assertTrue(rss.entry_set.all().exists())

        bulletin = Bulletin()
        bulletin.save()

        for entry in rss.entry_set.all():
            bulletin.entries.add(entry)

        output = bulletin.render().strip()
        self.assertTrue(output != '')

        client = Client()
        url = reverse("core:bulletin", args=(bulletin.id, ))
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
