# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20150618_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
