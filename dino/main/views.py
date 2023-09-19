from django.shortcuts import render

# Create your views here.
def index(request):
    
    # text = "Python"
    # a = 6
    # b = 44
    # return render(request, 'main/index.html', {'a':a, 'b':b})
    # message = ""
    
    # if request.method == 'POST':
    #     text = request.POST['name']
    #     message = "Your name is " + str(text)
    # return render(request, 'main/index.html', {'message':message})
    # message = ''
    # if request.method == 'POST':
    #     if request.POST['name'] != '':
    #         message = request.POST['name']
            
    #     else:
    #         message = "Enter the name "
    

      
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contactus(request):
    return render(request, 'main/contactus.html')

def printword(request):
    
    
    return render(request, 'main/printword.html')


