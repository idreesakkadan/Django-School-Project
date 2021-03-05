from django.shortcuts import render,redirect,HttpResponse
from .models import Student,Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='loginpage')
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def gallery(request):
    return render(request,'gallery.html')

def student(request):
    if request.method== 'GET':
        return render(request,'studentform.html')
    else:
        name=request.POST.get('name')
        classstd=request.POST.get('class')
        adno=request.POST.get('adno')
        place=request.POST.get('place')
        phone=request.POST.get('phone')

        addstd = Student.objects.create(name=name,class_std=classstd,ad_no=adno,place=place,phone=phone)
        return redirect(careers)
        
def teacher(request):
    if request.method == 'GET':
        return render(request,'teacherform.html')
    else:
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        email = request.POST.get('email')

        addtchr = Teacher.objects.create(name=name,department=dept,email=email)
        return redirect(home)

# career methode used to view students and fetch the data
def careers(request):
    #fFetch details of table Student of class 10.
    class_ten = Student.objects.filter(class_std='10')
    print(class_ten)

    # Fetch details of a Student of admission number 10030.
    adno_10030 = Student.objects.filter(ad_no='10030')
    print(adno_10030)
    
    viewstd = Student.objects.all()
    return render(request,'careers.html',{'data':viewstd})


def createuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginusr)
        else:
            return render(request,'registeruser.html',{'myform':form})
    else:
        form = UserCreationForm()
        return render(request,'registeruser.html',{'myform':form})



def loginusr(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        check = authenticate(request,username=username,password=password)
        if check:
            login(request,check)
            request.session['usertype']='admin'
            return redirect(home)
        else:
            return redirect(loginusr)

def logoutusr(request):
    logout(request)
    return redirect(loginusr)
