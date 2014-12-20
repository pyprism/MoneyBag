# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiren',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('amount', models.FloatField()),
                ('description', models.TextField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('tag', taggit.managers.TaggableManager(through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
