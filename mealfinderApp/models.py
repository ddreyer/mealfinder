# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    items = ListField()
