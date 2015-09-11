# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0007_desinationrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_id', models.IntegerField()),
                ('destination', models.ForeignKey(to='status.Status')),
            ],
        ),
        migrations.RemoveField(
            model_name='desinationrecord',
            name='destination',
        ),
        migrations.DeleteModel(
            name='DesinationRecord',
        ),
    ]
