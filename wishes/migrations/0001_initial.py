# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='T\xedtulo')),
                ('description', models.TextField(max_length=1024, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Desejo',
                'verbose_name_plural': 'Desejos',
            },
        ),
    ]
