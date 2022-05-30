from datetime import datetime
from distutils.ccompiler import gen_lib_options
from django.shortcuts import redirect, render
from psutil import users
from pytz import utc
from config.sms import send_otp_to_validate_phone

from users.models import Account

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.hashers import make_password

def index(request):
    username = password = ''

    if request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        # password = make_password('password')
        # print(password)
        user = authenticate(username=email, password=password)
        # if user is not None:
        login(request,user)
        print("Authenticated")
        acc = Account.objects.all()

        if user.is_authenticated:
            return redirect('users:customer_home')


    return render(request, 'index.html')

def customer_home(request):

    def get_patners():
        if request.user.wants == "Male":
            users = Account.objects.filter(gender="Male",wants="Male")
            return users
    
        if request.user.wants == "Female":
            users = Account.objects.filter(gender="Female",wants="Female")

            return users
        
        if request.user.wants == "Female":
            users = Account.objects.filter(wants="Male")

            return users
    
        if request.user.wants == "Trans-Gender":
            users = Account.objects.filter(gender="Trans-Gender")
            return users
    
    data = {
        'users': get_patners()
    }
    return render(request, 'customer/home.html',data)

def chat(request):
    return render(request, 'customer/chat.html')

def engineer_home(request):
    return render(request, 'engineer/home.html')


def register(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        pin = request.POST.get('password')
        gender = request.POST.get('gender')
        wants = request.POST.get('wants')
        avatar = request.POST.get('avatar')
        print(username)
        print(phone)
        print(age)
        print(avatar)
        print(gender)
        print(wants)

        if int(age) <= 18:
            print("You are bellow 18 years")
            messages.info(request, f"You are bellow 18 years")
            return redirect('users:register')

        #if phone number starts with 07 remove the 0 and add +254
        if phone[0] == '0':
            phone = phone[1:]
            phone = '+254'+phone
        
        #if phone number does not start with + append + 
        elif phone[0] != '+':
            phone = '+'+phone

        #check if the phone number is already registered
        if Account.objects.filter(phone_number=phone).exists():
            print("phone number already registered")
            messages.info(request, f"Phone number already registered")
            return redirect('users:register')

    

        #     create a custom user with the phone number as the username and email backend as the password
        parent = Account(
            phone_number = phone,
            user_name = username,
            age = age,
            password=make_password(pin),
            email = phone + "@gmail.com",
            gender = gender,
            wants = wants,
            avatar = avatar,
        )

        parent.is_customer = True
        
        parent.save()
        messages.info(request, f"You are now registered as {username}")

        user = authenticate(request,username=phone,password=pin)
        login(request,parent)

        print("Authenticated")

        return redirect('otp/?phone='+phone)

    # except:
    #     return redirect('users:ptc-register')
    print("Done")

    return render(request,'register.html',data)

