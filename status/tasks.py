from __future__ import absolute_import

from celery import shared_task
from datetime import datetime
from django.conf import settings
from rest_framework import status
from dateutil import parser as date_parser
from status.models import DestinationRecord

import requests
import json


@shared_task
def post_status_to_corecon(data):
    s = requests.Session()

    resp = s.get('http://corecondev.prod.acquia-sites.com/services/session/token')

    s.headers.update({'X-CSRF-Token': resp.text, 'Content-Type': 'application/json'})

    user_data = {'username': settings.STATUSHUB_USER, 'password': settings.STATUSHUB_PASSWORD}
    resp = s.post('http://corecondev.prod.acquia-sites.com/api/v1/test_service/user/login', data=json.dumps(user_data))

    assert resp.status_code == status.HTTP_200_OK

    start_date = date_parser.parse(data['start_date'])
    end_date = date_parser.parse(data['end_date'])

    req_data = {
        'field_start_date': {
            'und': [
                {
                    'value': {
                        'date': start_date.strftime('%m/%d/%Y - %H:%M:%S')
                    }
                }
            ]
        },
        'field_end_date': {
            'und': [
                {
                    'value': {
                        'date': end_date.strftime('%m/%d/%Y - %H:%M:%S')
                    }
                }
            ]
        },
        'field_description': data['description'],
        'title': data['title'],
        'type': 'status'
    }

    resp = s.get('http://corecondev.prod.acquia-sites.com/services/session/token')
    s.headers.update({'X-CSRF-Token': resp.text, 'Content-Type': 'application/json'})

    resp = s.post('http://corecondev.prod.acquia-sites.com/api/v1/test_service/node', data=json.dumps(req_data))
    assert resp.status_code == status.HTTP_200_OK
