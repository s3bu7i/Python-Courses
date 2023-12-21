import os

from celery import Celery

from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')

app = Celery('task')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# # a job is scheduled to run every five hours
# crontab(hour="*/5")
# # a job is scheduled to run every seventeen minutes
# crontab(minute="*/17")
# # a job is scheduled to run every two minutes during the second

# # half of each hour
# crontab(minute="30-59/2")
# # a job is scheduled to run at the top of every hour from 6am to 6pm # and runs after every three hours thereafter
# crontab(hour="*/3,6-18")


# # a job is scheduled to run for every minute in the first quarter of 
# # each hour
# crontab(minute="0-15")
# # a job is scheduled to run at 1am on weekdays only
# crontab(day_of_week="1-5", hour=1, minute=0)
# # a job is scheduled to run on the first five days of every month at # 7:30 am
# crontab(day_of_month="1-5", hour=7, minute=30)


# # a job is scheduled to run for every minute of every day
# crontab(minute="*")
# # a job is scheduled to run for every minute between 1am and 2am
# crontab(hour=1, minute="*")
# # a job is scheduled to run for every first minute of every hour
# crontab(hour="*", minute=1)


app.conf.beat_schedule = {
    
    'cron':{
        'task':'main.tasks.delete_db',
        'schedule':crontab(minute="*")
    }
    
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


