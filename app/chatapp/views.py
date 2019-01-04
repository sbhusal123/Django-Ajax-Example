from django.shortcuts import render
from .models import Messages

# Create your views here.

def index(request):
    message_list = Messages.objects.all()
    if request.method == 'POST':
        user = request.POST['name']
        message = request.POST['msg']
        Messages.objects.create(user=user,message=message)
        return render(request, 'app/index.html', {'message': message_list})


    return render(request,'app/index.html',{'message':message_list})

def refresh(request):
    message_list = Messages.objects.all()
    return render(request,'app/chatrefresher.html',{'message':message_list})