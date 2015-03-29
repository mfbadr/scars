# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('browser', models.CharField(max_length=128)),
                ('os', models.CharField(max_length=128)),
                ('device', models.CharField(max_length=128)),
                ('is_mobile', models.BooleanField()),
                ('is_tablet', models.BooleanField()),
                ('is_pc', models.BooleanField()),
                ('is_bot', models.BooleanField()),
            ],
        ),
    ]
