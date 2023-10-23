from django.shortcuts import render,redirect
from . models import *
import datetime
from django.core.mail import send_mail
from django.conf import settings




def index(request):
    
    data = Test.objects.raw(" SELECT * FROM main_test GROUP BY category")
    
    say = Test.objects.filter(category = "Golang").values().count()
    say1 = Test.objects.filter(category = "python").count()

    content = Test.objects.filter(category = "Golang").values_list("img","metn","basliq")

    test = Test.objects.all()[0:2]
    sec = Test.objects.all()[2:8]
    b = Test.objects.all()[8:9]
    c = Test.objects.all()[9:15]
    d = Test.objects.all()[0:5]
    f = Test.objects.all()[13:15]
    p = Test.objects.all()[7:10]
    # test = Test.objects.values_list("category","metn")
    
    
    
    # test1 = Test.objects.all().values()

    context = {
        
        'data':data,
        'say1':say1,
        'say':say,
        'content':content,
        'test':test,
        'sec':sec,
        'b':b,
        'c':c,
        'd':d,
        'f':f,
        'p':p
    }
    return render(request,'main/index.html',context)


def about(request):
    return render(request,'main/about.html')



def contact(request):
    
    return render(request,'main/contact.html')

def test_db(request):
    data = Test.objects.raw(" SELECT category FROM main_test GROUP BY category")
    return render(request,'main/test_db.html')

def category(request,id):
    
    data = Test.objects.get(id = id)
    
    a = data.category
    
    test = Test.objects.filter(category = a)
    
    return render(request,'main/category.html',{'test':test})



def blog_post(request,id):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        comment_id = request.POST['comment_id']
        test = Comment(name=name, email=email, message=message,comment_id=comment_id)
        test.save()
        
        
    comments = Comment.objects.filter(comment_id = id)

    
    
    data = Test.objects.filter(id=id)
    return render(request,'main/blog-post.html',{'data':data,'comments':comments,'id':id})


def send__mail(request):   
    
    subject = request.POST['subject'] , request.POST['email']
    message = request.POST['text']
    
    email_from = request.user.email
    recipient_list =   [ "nuraynecefli2001@gmail.com" ]

    send_mail( subject, message, email_from, recipient_list )
    
    return redirect('contact')

def search(request):
    if request.method == 'POST':
        src = request.POST['search']
        alltodos = Test.objects.filter(basliq__icontains = src)
        
        context = {
            
            'alltodos':alltodos
            
        }
        return render(request,'main/search.html', context)
    else:
        return redirect('index')
# def search(request):
#     src = request.POST['search']
#     alltodos = Test.objects.filter()
    
#     context = {
        
#         'alltodos':alltodos
        
#     }
#     return render(request,'list.html', context)
