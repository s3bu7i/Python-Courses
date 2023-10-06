from django.shortcuts import render,redirect
import qrcode
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User , auth
from  django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . models import CustomUser
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
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


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

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('index')
            
    
    return render(request, 'main/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')







