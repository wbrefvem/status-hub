# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0006_auto_20150819_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesinationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record_id', models.IntegerField()),
                ('destination', models.ForeignKey(to='status.Status')),
            ],
        ),
    ]
