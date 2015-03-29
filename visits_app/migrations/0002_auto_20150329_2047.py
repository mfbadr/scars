# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='browser_version',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='os_version',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='summary',
            field=models.CharField(default=None, max_length=256),
            preserve_default=False,
        ),
    ]
