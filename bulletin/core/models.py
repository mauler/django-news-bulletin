#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.template import Context, Template
from django.db import models

from dateutil.parser import parse
import feedparser


class Rss(models.Model):
    url = models.URLField(unique=True)

    def save(self, *args, **kwargs):
        new = self.pk is None
        saved = super(Rss, self).save(*args, **kwargs)
        if new:
            d = feedparser.parse(self.url)
            for entry in d["entries"]:
                self.entry_set.create(
                    title=entry['title'],
                    summary=entry['summary'],
                    link=entry['link'],
                    published=parse(entry['published']))

        return saved


class Entry(models.Model):
    rss = models.ForeignKey("Rss")
    title = models.TextField()
    summary = models.TextField()
    link = models.URLField(verify_exists=False)
    published = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Bulletin(models.Model):
    entries = models.ManyToManyField("Entry")

    def get_absolute_url(self):
        return reverse("core:bulletin", args=(self.pk, ))

    def render(self):
        t = Template(u"""<ul>
    {% for entry in entries %}
    <li>
        {{ entry }}
    </li>
    {% endfor %}
</ul>""")
        return t.render(Context({
            'bulletin': self,
            'entries': self.entries.all(),
        }))
