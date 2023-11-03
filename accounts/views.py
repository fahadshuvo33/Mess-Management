from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegistrationForm  
from accounts.models import CustomUser, Mess , Mess_Admin
from django.contrib.auth import get_user_model


def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or dashboard
            return redirect('dashboard')  # Replace 'dashboard' with the actual URL name
        else:
            # Handle invalid login credentials (e.g., show an error message)
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

def RegisterPage(request):
    if request.method == 'POST':
        mess_name = request.POST.get('mess_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        mess_admin = Mess_Admin.objects.create(name=username)
        mess_admin.save()
        mess = Mess.objects.create(name=mess_name,admin=mess_admin)
        mess.save()

        user = CustomUser.objects.create(
            username=username,
            email=email,
            phone=phone,
            is_admin=True,
            mess = mess
        )
        user.set_password(password)
        user.save()

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 

    return render(request, 'register.html')



def add_member(request):
    mess = request.user.mess
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        user = CustomUser.objects.create(
            mess = mess,
            username=username,
            email=email,
            phone=phone,
            is_admin=False
        )
        user.set_password(password)
        user.save()
        return redirect('members_info')

    return render(request,'add_member.html')


def LogoutPage(request) :
    logout(request)
    return redirect(reverse('login'))
