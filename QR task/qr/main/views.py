from django.shortcuts import render
import qrcode
# Create your views here.


def index(request):
    data = ''
    if request.method == 'POST':
        data = request.POST['qr']
        img = qrcode.make(data)
        img.save('static/images/test.png')
    
    return render(request, 'main/index.html',{'data':data})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')