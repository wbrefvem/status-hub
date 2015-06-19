# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20150618_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='start_date',
            field=models.DateField(),
        ),
    ]
