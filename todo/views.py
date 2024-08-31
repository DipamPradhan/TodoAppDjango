from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from todo import models
from todo.models import Task
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages


# Create your views here.


# @login_required(login_url="/login/")
def home(request):
    return render(request, "todo/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, email, password1, password2)

        if password1 != password2:
            messages.error(request, "Passwords doesnot match")
            return render(request, "todo/signup.html")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "todo/signup.html")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "todo/signup.html")
        my_user = User.objects.create_user(username, email, password1)
        my_user.save()
        messages.success(request, "User Created Successfully")
        return redirect("/login")
    return render(request, "todo/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        userr = authenticate(request, username=username, password=password)
        if userr is not None:
            login(request, userr)
            return redirect("/todopage")
        else:
            messages.error(request, "Username and Password doesnot match")
            return redirect("/login")

    return render(request, "todo/login.html")


@login_required(login_url="/login")
def todopage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        updatedAt = request.POST.get("updatedAt")
        priority = request.POST.get("priority")

        user = request.user
        obj = models.Task(
            title=title,
            updatedAt=updatedAt,
            priority=priority,
            user=user,
        )
        obj.save()

        res = models.Task.objects.filter(user=user).order_by("-priority")
        return redirect("/todopage", {"res": res})

    res = models.Task.objects.filter(user=request.user).order_by("-priority")
    return render(request, "todo/todopage.html", {"res": res})


def deleteTodo(request, srno):
    obj = models.Task.objects.get(srno=srno)
    obj.delete()

    return redirect("/todopage")


@login_required(login_url="/login")
def editTodo(request, srno):
    if request.method == "POST":
        title = request.POST.get("title")
        updatedAt = request.POST.get("updatedAt")
        priority = request.POST.get("priority")
        obj = models.Task.objects.get(srno=srno)
        obj.title = title
        obj.updatedAt = updatedAt
        obj.priority = priority
        obj.save()

        return redirect("/todopage")
    obj = models.Task.objects.get(srno=srno)
    return render(request, "todo/editTodo.html", {"obj": obj})


def signout(request):
    logout(request)
    return redirect("/login")
