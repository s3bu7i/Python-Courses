from django.shortcuts import render
from store.models import *

def index(request):
    products = Product.objects.filter(is_avialable=True)
    context = {
        'products':products,}
    
    return render(request, 'index.html', context)

# Create your views here.
