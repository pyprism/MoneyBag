# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiren',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('amount', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('tag', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
