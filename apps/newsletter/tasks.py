from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task


@task(name="test_task")
def test_task():

    print("testing Celery task")

    return None

