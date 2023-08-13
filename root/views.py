from django.shortcuts import render
from .models import Service

# Create your views here.







def home(request):
    service  = Service.objects.filter(status=True)
    context = {
        'services':service
    }
    return render(request,"root/index.html",context=context)

def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")