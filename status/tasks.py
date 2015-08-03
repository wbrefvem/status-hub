from __future__ import absolute_import

from celery import shared_task

import requests


@shared_task
def post_status_to_corecon(data):
    print "You're soooooooo good looking"
    print data
