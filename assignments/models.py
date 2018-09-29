# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Assignments(models.Model):
    ass_no  =    models.IntegerField()
    subject =    models.CharField(max_length =5)
    title   =    models.CharField(max_length=1000)
    slug    =    models.SlugField()
    body    =    models.TextField()
    date    =    models.DateField(auto_now_add=True)

    submit = models.DateField()

    document =  models.FileField()
    #add in thumbnail
    #add in author


    def __unicode__(self):
        return unicode(self.title)

    def snippet(self):
        return self.body[:200]+'.....'
