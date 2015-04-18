# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daoService', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(related_name='publishs', blank=True, to='daoService.User'),
        ),
    ]
