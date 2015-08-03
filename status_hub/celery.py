from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'status_hub.settings')

app = Celery('status_hub')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)




@app.task()
def add(x, y):
    print "You're soooooooo good looking"
    return x + y
