# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
from django.utils import timezone


class Wish(models.Model):
    title = models.CharField(u'Título', max_length=128)
    description = models.TextField(u'Descrição', max_length=1024)
    created_at = models.DateTimeField(u"Data de criação", default=timezone.now)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Desejo'
        verbose_name_plural = u'Desejos'
