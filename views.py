from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

import random
import time

# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = 0
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name,)
                user.save();
                print('user Created')
                return redirect('login')
        else:
            messages.info(request,'user not Created,Password Mismatch ')
            return redirect('register')

        
        

    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def contact(request):
    return render(request,"contactpg.html")

def game(request):
    numbers = (1,2,3,4,5,6)
    d1 = random.choice(numbers)
    d2 = random.choice(numbers)
    dice2 = d1+d2
    print(F"hi number is {dice2}")
    return render(request,"dice.html",{'dicevalue':dice2,'Dicev1':d1,'Dicev2':d2})
    time.sleep(5.0)
        




