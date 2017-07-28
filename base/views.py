from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from accounting.helpers import AccHelper
from django.db import IntegrityError,transaction
from django.contrib.auth.decorators import login_required

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
            user_exists = User.objects.filter(email=email)
            if user_exists:
                messages.error(request, "Account already exists!")
                return redirect('register')
            else:
                with transaction.atomic():
                    try:
                        user = User.objects.create_user(username=username,
                                                        email=email,
                                                        password=password)
                        AccHelper.create_all_basic_acc_heads(user)
                        return render(request, 'base/thanks.html')
                    except IntegrityError:
                        messages.error(request, "Internal error! Contact with support.")
                        return redirect('register')

        else:
            messages.error(request, 'Password did not match!')
            return redirect('register')
    else:
        return render(request, 'base/sign_up.html')

@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')

@login_required
def logout(request):
    messages.add_message(request, messages.SUCCESS, 'Your are successfully logged out.')
    auth.logout(request)
    return redirect('login')
