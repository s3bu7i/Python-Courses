from django.shortcuts import render

# Create your views here.


def index(request):
    num1 = 1
    num2 = 2
    num3 = 3
    
    context = {
        'data1': num1,
        'data2': num2,
        'data3': num3
    }
    
    return render(request, 'main/index.html', {'context': context})    

