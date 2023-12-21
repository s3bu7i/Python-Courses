from django.shortcuts import render , HttpResponse
from .tasks import result,send_mail_celery,delete_db
from . models import Result


# result.delay()

# send_mail_celery.delay()

delete_db.delay()

# lte kicik beraberdir
data = Result.objects.filter(num__lte = 100)
# gte boyuk  beraberdir
data = Result.objects.filter(num__gte = 100)



# Result.objects.filter(num__gte = 100)


def home(request):
    data = result.delay()
   
    return render(request,'home.html')