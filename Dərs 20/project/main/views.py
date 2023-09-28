from django.shortcuts import render , redirect
from .models import *
from django.urls import reverse
from django.contrib import messages
from .forms import StudentForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView



class Etrafli(DetailView):
    template_name = 'main/etrafli.html'
    model = Telefon
    context_object_name = 'x'



def index(request):
    
  
    
    # mesaj = ''
    # if request.method == 'POST':
        
    #     mesaj = request.POST['ad'] + ' '+ request.POST['soyad'] + ' '+ request.POST['email']
        
    mesaj = ''
    
    if request.method == 'POST':
        text = request.POST['hesabla']
        mesaj = len(text.split())
  
    return render(request,'main/index.html',{'mesaj':mesaj,})

def calculator(request):
    
    # mesaj = ''
    # if request.method == 'POST':
    #     text = request.POST['cal']
    #     mesaj = eval(text)
    
    mesaj = ''
    
    if request.method == 'POST':
        
        text1 = int(request.POST['cal'])
        text2 = int(request.POST['cal1'])

        
        if '+' in request.POST:
            mesaj = text1 + text2
        if '-' in request.POST:
            mesaj = text1 - text2
        if '*' in request.POST:
            mesaj = text1 * text2
        if '/' in request.POST:
            mesaj = text1 / text2
        
    return render(request,'main/calculator.html',{'mesaj':mesaj})

def login(request):
    
    mesaj = ''
    
    if request.method == 'POST':
        
        if request.POST['login'] == 'nasib' and request.POST['parol'] == '12345':
            mesaj = 'Xos geldiniz'
        elif request.POST['login'] == '' and request.POST['parol'] != '':
            mesaj = 'Zehmet olmasa logini daxil edin '
        elif request.POST['login'] != '' and request.POST['parol'] == '':
            mesaj = 'Zehmet olmasa parolu daxil edin '
        elif request.POST['login'] != 'nasib' and request.POST['parol'] == '12345':
            mesaj = 'Login yanlishdir'
        elif request.POST['login'] == 'nasib' and request.POST['parol'] != '12345':
            mesaj = 'Parol yanlishdir'
        elif request.POST['login'] == '' and request.POST['parol'] == '':
            mesaj = 'Login ve parolu daxil edin '
        else:
            mesaj = 'Login ve parol yanlishdir'
            
    return render(request,'main/login.html',{'mesaj':mesaj})

def about(request):
  
    step = 1
    error = ''
    mesaj = ''
    
    if request.method == 'POST':
    
        
        if 'step1' in request.POST:
            
            if   request.POST['ad'] == '' or request.POST['soyad'] == '':
                step = 1
                error = 'Xanalari Doldurun'
            else:
                ad = request.POST['ad']
                step = 2
                
        elif 'step2' in request.POST:

            if request.POST['email'] == '' or request.POST['yash'] == '':
                step = 2
                error = 'Xanalari Doldurun'
            else:
                step = 3
                
        elif 'step3' in request.POST:

            
            if request.POST['maash'] == '' or request.POST['mebleg'] == '':
                step = 3
                error = 'Xanalari Doldurun'
            else:
                mebleg = int(request.POST['mebleg'])
                maash = int(request.POST['maash'])
                
                
                if mebleg < 10:
                    step = 3
                    
                    error = 'Minimum 10 azn daxil ede bilersiniz '
                elif mebleg>1000:
                    step = 3
                    
                    error = 'Maksimum mebleg 1000 AZN olmalidir'

                elif maash < 500 and mebleg > 10 and mebleg < 1000:
                    mesaj =' Sizin '  + str((mebleg * 50) / 100) +' azn desteyiniz qebul olundu'
                    step = 4
                    
                elif maash > 500 and mebleg > 10 and mebleg < 1000 :
                    mesaj = ' Sizin '+str(ad)+ ''  + str(mebleg) +' azn desteyiniz qebul olundu'
                    step = 4
                    
               
               
        
    return render(request,'main/haqqinda.html',{'error':error,'mesaj':mesaj,'step':step})

def elaqe(request):
    
    
    
    
    return render(request,'main/elaqe.html')

def radio(request):
    mesaj = ''
    
    text = ''
    
    if request.method == 'POST':
        text = request.POST['s1']
        if 's1' in request.POST:
            
         
            mesaj = 'Salam '+request.POST['s1']
            
 
    context = {
        
        'mesaj': mesaj,
        'text':text
        
    }
             
    return render(request,'main/radio.html',context)


# Exam


def exam(request):
    
    dogru = 0
    yanlish = 0
    bal = 0
    
    if request.method == 'POST':
    
        if 'cavab1' in request.POST:
            
            if request.POST['cavab1'] == 'a':
                dogru +=1
            elif request.POST['cavab1'] !=  '' and request.POST['cavab1'] != 'a':
                yanlish +=1
        if 'cavab2' in request.POST:
            
            if request.POST['cavab2'] == 'b':
                dogru +=1
            elif request.POST['cavab2'] !=  '' and request.POST['cavab2'] != 'b':
                yanlish +=1      
        
        if 'cavab3' in request.POST:
            
            if request.POST['cavab3'] == 'c':
                dogru +=1
            elif request.POST['cavab3'] !=  '' and request.POST['cavab3'] != 'c':
                yanlish +=1       
                
        if 'cavab4' in request.POST:
            
            if request.POST['cavab4'] == 'd':
                dogru +=1
            elif request.POST['cavab4'] !=  '' and request.POST['cavab4'] != 'd':
                yanlish +=1     
    
    
        if 'cavab5' in request.POST:
            
            if request.POST['cavab5'] == 'd':
                dogru +=1
            elif request.POST['cavab5'] !=  '' and request.POST['cavab5'] != 'd':
                yanlish +=1
                
        while yanlish  == 3:
            dogru -= 1
            break
        
    bal = dogru * 10

    return render(request,'main/exam.html',{'dogru':dogru,'yanlish':yanlish,'bal':bal})


def select(request):
    ad = ''
    mesaj = ''
    if request.method == 'POST':
        ad = request.POST['ad']
        if request.POST['ad'] != '':
            mesaj = 'Sizin vezifeniz ' + request.POST['ad']
            
        else:
            mesaj = 'Xahis edirik secim edin '
    
    
    return render(request,'main/select.html',{'mesaj':mesaj,'ad':ad})

def select_exchange(request):
    
    mesaj = ''
    
    exchange_az = {'usd': 0.59 ,'eur': 0.54 }
    
    exchange_usd = {'azn':1.7,'eur':0.94}
    exchange_eur = {'azn':1.81,'usd':1.07 }
    
    if request.method == 'POST':
        
        # AZN TO USD
        if request.POST['al'] == 'azn' and request.POST['sat'] == 'usd':
            
            num = float(request.POST['secim']) * exchange_az['usd']
            mesaj = str(request.POST['secim']) + ' AZN = ' + str(num) +' USD' 
            
        # AZN TO EUR    
        elif request.POST['al'] == 'azn' and request.POST['sat'] == 'eur':
            num = float(request.POST['secim']) * exchange_az['eur']
            mesaj = str(request.POST['secim']) + ' AZN = ' + str(num) + 'EUR'
            
            
        elif request.POST['al'] == 'usd' and request.POST['sat'] == 'azn':
            num = float(request.POST['secim']) * exchange_usd['azn']
            mesaj = str(request.POST['secim']) + ' USD = ' +str(num) + ' AZN'
            
        elif request.POST['al'] == 'usd' and request.POST['sat'] == 'eur':
            num = float(request.POST['secim']) * exchange_usd['eur']
            mesaj = str(request.POST['secim']) + ' USD = ' +str(num) + ' EUR '
            
        
        elif request.POST['al'] == 'eur' and request.POST['sat'] == 'azn':
            num = float(request.POST['secim']) * exchange_eur['azn']
            mesaj = str(request.POST['secim']) + ' EUR = ' + str(num) + ' AZN'
            
        elif request.POST['al'] == 'eur' and request.POST['sat'] == 'usd':
            num = float(request.POST['secim']) * exchange_eur['usd']
            mesaj = str(request.POST['secim']) + ' EUR = ' + str(num) + ' USD'
    
    return render(request,'main/select_exchange.html',{'mesaj':mesaj})

def step(request):
    
    mesaj = ''
    addim = 1
    error = ''
    
    if request.method == 'POST':
        
        if 'step1' in request.POST:
            
            if request.POST['ad'] == '' and request.POST['soyad'] == '':
                addim = 1
                error = 'Xanalari doldurun'
            else:
                addim = 2 
                
    
        
        if 'step2' in request.POST:
            
            if request.POST['email'] == '' and request.POST['yash'] == '':
                addim = 2
                error = 'Xanalari doldurun'
            else:
                addim = 3

        if 'step3' in request.POST:
            
            if request.POST['maash'] == '' and request.POST['mebleg'] == '':
                addim = 3
                error = 'Xanalari doldurun'
            else:
                
                mebleg = int(request.POST['mebleg'])
                maash = int(request.POST['maash'])
                
                if mebleg < 10:
                    addim = 3
                    error = 'minimum 10 azn daxil ede bilersiniz'

                if mebleg > 1000:
                    addim = 3
                    error = 'maksimum 1000 azn daxil ede bilersiniz'
                    
                    
                if maash < 500 and mebleg > 10 and mebleg < 1000:
                    addim = 4
                    mesaj = 'Sizin ' +str((mebleg * 50 / 100)) + ' mebleginiz qebul olundu'
                if maash > 500 and mebleg > 10 and mebleg < 1000:
                    addim = 4
                    mesaj = 'Sizin ' + str(mebleg) + ' mebleginiz qebul olundu'
        
    return render(request,'main/step.html',{'mesaj':mesaj,'addim':addim,'error':error})

def crud(request):
    
   
    # data = Student.objects.all().order_by('-id')
    
    data = Student.objects.all()
    
    say = Student.objects.all().count()
    
    if request.method == 'POST':
        
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        
    
    form = StudentForm()
        
        
        
        # data = Student(ad = request.POST['ad'],metn = request.POST['metn'])
        # data.save()
        
    
    context = {
        
        'data':data,
        'say':say,
        'student':form
       

        
    }
    
    return render(request,'main/crud.html',context)




def tesdiq(request,id):
    tesdiq = Student.objects.get(id=id)
    
    
    data = Student.objects.all()
    
    say = Student.objects.all().count()
    
    return render(request,'main/crud.html',{
        
        'tesdiq':tesdiq,
        'data':data,
        'say':say,
       
        
        })


def delete(request,pk):
    
    data = Student.objects.get(id=pk)
    data.delete()
    
    messages.success(request,' Melumat Ugurla silindi')
    
    return redirect('crud')

# def delete(request):
    
#     for x in request.POST.getlist('x[]'):
#         Student.objects.get(id=x).delete()
       
#     return redirect('crud')

def edit(request,id):
    
    
    
    edit = Student.objects.get(id=id)
    
    data = Student.objects.all()
    
    say = Student.objects.all().count()
    
    
    context = {
        
        'edit':edit,
        'data':data,
        'say':say,
        
        
    }
    
    return render(request,'main/crud.html',context)

# foto=request.FILES['foto']
#         fs = FileSystemStorage()
#         filename=fs.save(foto.name,foto)
#         uploaded_file_url=fs.url(filename)

def update(request,id):
    
    ad = request.POST['ad']
    metn = request.POST['metn']
    
    data = Student.objects.get(id=id)
    
    data.ad = ad
    data.metn = metn
    data.save()
    messages.success(request,'Melmat Ugurla yenilendi')
    
    return redirect('crud')



def telefon(request):
    
    if request.method=='POST' :
        foto=request.FILES['foto']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)
        data = Telefon(img = uploaded_file_url)
        data.save()
    


     
    data = Telefon.objects.all()
    
    say = Telefon.objects.all().count()
    
    context = {
        
        'data': data,
        'say': say
        
    }
    
    return render(request,'main/telefon.html',context)






def shop(request):
    data = Shop.objects.all()
    return render(request,'main/shop.html',{'data':data})