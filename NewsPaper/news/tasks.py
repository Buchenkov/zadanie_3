from celery import shared_task

@shared_task
def text():
    print('Hello')