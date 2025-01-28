from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from student.models import Student
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    query = request.GET.get('q', '')
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(course__icontains=query)
        )
    return render(request,'home.html', {'students':students})

def create_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        course = request.POST.get('course')
        address = request.POST.get('address')
        
        new_student = Student.objects.create(name=name, roll=rollno, course=course, address=address)
        return redirect('home')
    
    return render(request, 'form.html')

def details(request, pk):
    stu = Student.objects.get(id=pk)
    return render(request, 'details.html', {'student':stu})


def update_student(request, pk):
    stu = Student.objects.get(id=pk)
    if request.method == 'POST':
        stu.name = request.POST.get('name')
        stu.roll = request.POST.get('rollno')
        stu.course = request.POST.get('course')
        stu.address = request.POST.get('address')
        stu.save()
        return redirect(reverse('details', args=[stu.id]))
    
    return render(request, 'form.html',{'student':stu})


def delete_stu(request, pk):
    stu = Student.objects.get(id=pk)
    if request.method == "POST":
        stu.delete()
        return redirect('home')

    return render(request, 'delete.html', {'student': stu})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f'Contact Form Message from {name}',
            message,  
            email,
            [settings.CONTACT_EMAIL], 
            fail_silently=False,
        )

        send_mail(
            'Thank you for contacting us!',
            'We have received your message and will get back to you shortly.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'contact.html')

def singup(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        email=request.POST.get('email')
        pw1=request.POST.get('pw1')
        pw2=request.POST.get('pw2')

        if pw1 == pw2 :
            if User.objects.filter(username=un):
                context={'msg':'User already exists !!'}
                return render(request,'singup.html',context)
            else:
                User.objects.create_user(
                    username=un,
                    email=email,
                    password=pw1
                )
                return redirect('singup')
        else:
            context={'msg':'Password Does not match !!'}
            return render(request,'singup.html',context)
        
    return render(request,'singup.html')
            
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    
    if request.method =='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')

        user=authenticate(request,username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return render(request,'login.html',{'msg':'Enter Valid Credentials!!'})
        
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
