from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    """
    Handles authentication
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect('/')
    else:
        return render(request, 'base/login.html')


def register(request):
    """
    Handles registration
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
            except:
                messages.error(request, "Account already exists!")
                return redirect('register')
            if user:
                return render(request, 'base/thanks.html')
        else:
            messages.error(request, 'Form is not valid!')
            return redirect('register')
    else:
        return render(request, 'base/sign_up.html')
