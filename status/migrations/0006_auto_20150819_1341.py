# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0005_auto_20150624_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='url',
        ),
        migrations.AddField(
            model_name='status',
            name='destinations',
            field=models.ManyToManyField(to='status.Destination'),
        ),
    ]
