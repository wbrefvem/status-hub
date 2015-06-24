# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20150619_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='url',
            field=models.CharField(default='http://www.raleighnc.gov', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
