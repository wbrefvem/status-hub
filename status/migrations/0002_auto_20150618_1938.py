# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='contact',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='date',
            new_name='end_date',
        ),
        migrations.RemoveField(
            model_name='status',
            name='department',
        ),
        migrations.RemoveField(
            model_name='status',
            name='message',
        ),
        migrations.RemoveField(
            model_name='status',
            name='state',
        ),
        migrations.AddField(
            model_name='status',
            name='description',
            field=models.TextField(default='Default Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 19, 38, 11, 827064)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='title',
            field=models.CharField(default='Default Title', max_length=256),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
