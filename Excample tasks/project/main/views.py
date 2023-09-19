from django.shortcuts import render

# Create your views here.



def index(request):
    
    # mesaj = ''
    # if request.method == 'POST':
        
    #     mesaj = request.POST['ad'] + ' '+ request.POST['soyad'] + ' '+ request.POST['email']
        
    mesaj = ''
    
    if request.method == 'POST':
        text = request.POST['hesabla']
        mesaj = len(text.split())
  
    return render(request,'main/index.html',{'mesaj':mesaj})

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

def about(request):
    return render(request,'main/haqqinda.html')

def elaqe(request):
    return render(request,'main/elaqe.html')