from celery import Celery
from status.models import Status

app = Celery('tasks')


@app.task
def add(x, y):
    print "You're soooooooo good looking"
    return x + y
