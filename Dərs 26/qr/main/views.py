from django.shortcuts import render,redirect
import qrcode
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , auth
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . models import CustomUser
from django.urls import reverse
User = get_user_model()


@login_required()
def index(request):
    imgs = CustomUser.objects.filter(id = request.user.id)
  
    data = ''
    if request.method == 'POST':
        data = request.POST['qr']
        img = qrcode.make(data)
        img.save('static/images/test.png')
    
    return render(request, 'main/index.html',{'data':data,'imgs':imgs})


def about(request):
    imgs = CustomUser.objects.filter(id = request.user.id)

    return render(request, 'main/about.html',{'imgs':imgs})


def contact(request):
    imgs = CustomUser.objects.filter(id = request.user.id)

    return render(request, 'main/contact.html',{'imgs':imgs})


def register(request):
    if request.method == 'POST':
        foto=request.FILES['foto']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)

        username = request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['pass']
        re_pass = request.POST['re_pass']
        
        if password == re_pass:
            
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,'Bu istifadeci hal-hazirda movcuddur')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Bu email hal-hazirda movcuddur')
            
            else:
                
                CustomUser.objects.create_user(img=uploaded_file_url,username=username,last_name=last_name,first_name=first_name,email=email,password=password).save()
                return redirect('login')
                
        else:
            messages.info(request,'Parollar uygun deyil')
            
   
    
    return render(request, 'main/register.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,request = request)
        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
            
    
    return render(request, 'main/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def settings(request):
    
    user_id = CustomUser.objects.all()
    
    
    userid = CustomUser.objects.get(id = request.user.id )
    
    
    imgs = CustomUser.objects.filter(id = request.user.id)

    return render(request, 'main/settings.html',{'imgs':imgs,'userid':userid,'user_id':user_id})

def updateprofile(request,id):
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_pass1 = request.POST['re_pass1']
        re_pass2 = request.POST['re_pass2']
        
        user = CustomUser.objects.get(id=id)
        
        if user.check_password(password):
            if request.method == 'POST' and 'foto' in request.FILES:
                foto=request.FILES['foto']
                fs = FileSystemStorage()
                filename=fs.save(foto.name,foto)
                uploaded_file_url=fs.url(filename)
                user.img = uploaded_file_url
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            
        else:
            messages.info(request,'Cari shifrenizi daxil edin')
            
        if user.check_password(password):
            if password != '' and re_pass1 != '' and re_pass2 != '':
                if re_pass1 == re_pass2:
                    user.set_password(re_pass2)
                    user.save()
                    return redirect('login')
                else:
                    messages.info(request,'Parollar uygun deyil')
                    
        user.save()

    return redirect('settings')


def block(request,id):
    
   userid = CustomUser.objects.get(id =id)
   userid.is_active = False
   userid.save()
   
   
   
   
   return redirect(reverse('settings'))

def active(request,id):
    userid = CustomUser.objects.get(id =id)
    userid.is_active = True
    userid.save()
   
   
   
   
    return redirect(reverse('settings'))
    
    
def error_page(request,exception):
    
    return render(request,'404.html',status=404)
    
    









