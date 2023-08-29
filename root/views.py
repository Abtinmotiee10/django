from django.shortcuts import render,redirect
from .models import Services
from courses.models import Course,Trainer
from courses.models import Category
from django.contrib.auth.models import User
from .forms import NewsLetterform


# Create your views here.



def home (request):
    if request.method == 'GET':
        service_count = Services.objects.filter(status=True).count()
        course_count = Course.objects.filter(status=True).count()
        trainer_count = Trainer.objects.filter(status=True).count()
        user_count = User.objects.filter(is_active=True).count()
        category = Category.objects.all()

        services = Services.objects.filter(status=True)
        last_three_course = Course.objects.filter(status=True)[:3]
        last_three_trainer = Trainer.objects.filter(status=True)[:3]
        context = {
            'service':services,
            'course':last_three_course,
            'trainer':last_three_trainer,
            'category':category,
            'sc' : service_count,
            'cc' : course_count,
            'tc' : trainer_count,
            'uc' : user_count,
        }
        return render(request,"root/index.html" , context=context)
    elif request.method == 'POST':
        new_email = NewsLetter()
        new_email.email = request.POST.get('email')
        new_email.save()
        return redirect('root:home')

def about (request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/about.html",context=context)

def contact(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/contact.html",context=context)



def trainer(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/trainers.html",context=context)