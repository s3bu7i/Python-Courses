from django.shortcuts import render, get_object_or_404
from . models import *
from category.models import *

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_avialable=True)
        products_counts = products.count()
    else:
        products = Product.objects.filter(is_avialable=True)
        products_counts = products.count()

    context = {
        'products':products,
        "products_counts":products_counts,
        
        }
    
    return render(request, 'store/store.html', context)




def product_detail(request,category_slug,products_slug):
    try:
        single_product =Product.objects.get(category__slug =category_slug, slug=products_slug)
        
    except Exception as e:
        raise e
    
    context= {
        
        "single_product":single_product,
    }
    
    return render( request, 'store/product_detail.html', context)
    
