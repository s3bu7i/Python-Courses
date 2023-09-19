from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def blogs(request):
    return HttpResponse('Blogs')

def blog_details(request, id):
    return HttpResponse('Blog Details: ' + str(id))

