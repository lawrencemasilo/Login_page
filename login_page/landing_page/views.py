from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_password = request.POST['f_password']

        user = authenticate(username=username, password=f_password)
        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            return messages.error(request, "Invalid Username/Password")
    return render(request, "landing_page.html")


def signup(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        f_password = request.POST['f_password']
        s_password = request.POST['s_password']
        if f_password == s_password:
            create_user = User.objects.create_user(username=username, password=f_password)
            create_user.first_name = f_name
            create_user.last_name = l_name

            create_user.save()
            return redirect("login_user")
    return render(request, "sign_up.html")


def signout(request):
    logout(request)
    return redirect("login_user")