from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Result
from django.db.models.functions import Now
from datetime import timedelta

@shared_task()
def result():
    
    for x in range(11):
        print(x)
    
    return 'Done'



@shared_task()
def send_mail_celery():
    
    send_mail(
        
        subject="Email Test",
        message="Salam",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list= ["nasiboffdev@gmail.com"],
        fail_silently= True
   
    )
    
    return 'Email Gonderildi'


@shared_task()
def delete_db():
    
    Result.objects.filter(tarix__lte = Now() - timedelta(seconds=30)).delete()
    
    
    return " Ugurla Silindi "

