# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.dateparse import parse_datetime
from django.utils.encoding import force_str
from django.db import models
from datetime import datetime
# Create your models here.:

class ISODateTimeField(models.DateTimeField):
    def strptime(self, value, format):
        return parse_datetime(force_str(value))

class Task(models.Model):
    title = models.CharField(blank=True, null=True, max_length=50)
    desc = models.TextField(blank=True, null=True)
    date_created = models.CharField(max_length=100,default = datetime.now().isoformat())
    #ago = models.CharField(max_length=100, default = timeago.format(datetime.now))
    done = models.BooleanField(default =False)
