from celery import shared_task


@shared_task()
def result():
    
    return 'Done'