from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "loginreg/loginreg.html")

def register(request):
    errors = Users.objects.basic_validator(request.POST)   
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginreg')
    else:
        new_user = Users(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"], passwordc=request.POST["passwordc"])
        new_user.save()
        request.session["id"] = new_user.id
        request.session["user"] = new_user.first_name
    return redirect("/success")

def login(request):
    created_user = Users.objects.filter(email=request.POST["email"])
    if created_user[0].password == request.POST["password"]:
        request.session["user"] = created_user[0].first_name
        request.session["id"] = created_user[0].id
        return redirect("/success")
    return redirect("/loginreg")

def success(request):
    if "user" not in request.session:
        return redirect('/loginreg')
    else:
        return render(request, "loginreg/success.html")

