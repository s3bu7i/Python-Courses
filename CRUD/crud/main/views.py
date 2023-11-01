from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *


# Create your views here.

@login_required()
def index(request):
    
    return render(request, "main/index.html" )

def signup(request):
     
    if request.method == 'POST':
        username = request.POST["username"] 
        email = request.POST["email"] 
        password1 = request.POST["pass1"] 
        password2 =  request.POST["pass2"]
        
        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists!')
                
            else:
                User.objects.create_user(username=username, email=email, password=password1)
                
                return redirect('sign_in')
        else:
            messages.info(request, "Password are not same!!")   
            
    return render(request, 'main/signup.html') 

 
def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"] 
        

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("index")
        
        
    return render(request, 'main/login.html')
                

def log_out(request):
    logout(request)
    return redirect('sign_in')
        
        
def crud(request):
     
    data=Crud.objects.all()
    say=Crud.objects.all().count()   
   
    if request.method== 'POST':
        
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        passw = request.POST['passw']
  
        listt= Crud(name=name, lname=lname,email=email, passw=passw )
        listt.save()
        messages.success(request,name+(' Ugurla elave edildi'))
        
        
        
    context={
        
        "data": data,
        'say':say
       
    }
        
 
    return render( request, 'main/crud.html', context )     




def delete(request,pk):
    
    data=Crud.objects.get(id=pk)
    data.delete()
   
    return redirect('crud')
  
        
        
        
def edit(request,id):
    
    edit=Crud.objects.get(id=id)
    
    data=Crud.objects.all()
    say=Crud.objects.all().count()
    
    context={
            
        "edit": edit,
        "data": data,
        'say':say,
         
        }
    return render( request, 'main/crud.html', context )   

def update(request,id):
    name = request.POST['name']
    lname = request.POST['lname']
    email = request.POST['email']
    passw = request.POST['passw']
    
    data=Crud.objects.get(id=id)
    
    data.name= name
    data.lname = lname
    data.email = email
    data.passw = passw
    data.save()
    
    return redirect('crud')