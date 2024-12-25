from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from student.models import Student
from django.db.models import Q

# Create your views here.
def home(request):
  
    return render(request,'home.html')

def create_student(request):

    
    
    return render(request, )

def details(request, pk):
    
    return render(request, 'details.html')


def update_student(request, pk):
   
    
    return render(request, 'form.html')


def delete_stu(request, pk):
    
    return render(request, 'delete.html')



def about(request):
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')