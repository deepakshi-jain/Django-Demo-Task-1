from django.shortcuts import render
from .models import Data,Dbt
from django.contrib.auth.models import User, auth


def book(request):
    return render(request, "navbar.html")


def login(request):
    if request.method == "POST":
        a=request.POST['pno']
        b=request.POST['a']
        user = auth.authenticate(username=b,password=a)
        if user is not None:
            request.session["is_logged"] = True
            auth.login(request, user)
            return render(request, "home.html")
    else:
        return render(request, "login.html")


def form(request):
    if request.method == "POST":
        grade = request.POST['grade']
        chce = request.POST['choice']
        shft = request.POST['shift']
        tme = request.POST['time']
        pname = request.POST['a']
        sname = request.POST['b']
        pno = request.POST['c']
        email = request.POST['d']
        obj = Data()
        obj.grade = grade
        obj.laptop = chce
        obj.shift = shft
        obj.time = tme
        obj.parentname = pname
        obj.stuname = sname
        obj.phoneno = pno
        obj.email = email
        obj.save()
        user = User.objects.create_user(username=sname,password=pno)
        user.save()
        return render(request, "bookformdetails.html", {"row": "Submitted Successfully"})
    else:
        return render(request, "bookformdetails.html")



def logout(request):
    auth.logout(request)
    return  render(request,"navbar.html")


def doubt(request):
    if request.method=="POST":
        question=request.POST['comment']
        file=request.POST['file']
        obj=Dbt()
        if question or file:
            obj.question=question
            obj.file=file
            obj.save()
        return render(request, "doubt.html",{'row':"Submitted Successfully"})
    else:
        return render(request,"doubt.html")