# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-12 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bAndA', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='bAndA.Book'),
        ),
    ]
