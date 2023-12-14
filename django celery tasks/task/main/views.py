from django.shortcuts import render , HttpResponse
from .tasks import result
# Create your views here.


result.delay()


def home(request):
    data = result.delay()
   
    return render(request,'home.html')