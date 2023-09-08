from django.shortcuts import render

# Create your views here.
def index(request):
    
    # text = "Python"
    # a = 6
    # b = 44
    # return render(request, 'main/index.html', {'a':a, 'b':b})
    message = ""
    
    if request.method == 'POST':
        text = request.POST['name']
        message = "Your name is " + str(text)
    
    return render(request, 'main/index.html', {'message':message})
