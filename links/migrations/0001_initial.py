# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=32, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('name', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=63)),
                ('category', models.ForeignKey(to='links.Category')),
            ],
        ),
    ]
