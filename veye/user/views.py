from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User


# Create your views here.
def hello(request):
    return HttpResponse("<h1>hello,world</h1>")

def register_form(request):
    return render(request,'user/register_form.html')

def register(request):
    email = request.POST['email']
    password = request.POST['password']
    password = make_password(password,hasher='pbkdf2_sha256')
    user = User(email=email,password=password)
    user.save()
    return HttpResponse('Registe success.')

def login_form(request):
    return render(request,'user/login_form.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.get(email=email)
    if check_password(password, user.password):
        response = HttpResponse('Login success.')
        response.set_cookie('login','True')
        return response
    else:
        return HttpResponse('Login failed.')

def logout(request):
    response = HttpResponse('Logout success.')
    response.set_cookie('login','False')
    return response
