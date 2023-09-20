from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def patient(request):
    if request.method=='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            request.session['sid'] = username
            if request.user.is_doctor or request.user.is_superuser:
                messages.error(request, "Login not permitted")
                logout(request)
            return redirect('/dashboard/patient')
        else:
            messages.error(request, "Incorrect Credentials")
    return render(request, 'login-patient.html')


def admin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('/dashboard/admin')
            else:
                messages.error(request, "Login not permitted")
                logout(request)
        else:
            messages.error(request, "Incorrect Credentials")
    return render(request, 'login-admin.html')


def medicalcen(request):
    if request.method=='POST':
            username = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if request.user.is_staff and not request.user.is_superuser:
                    return redirect('/dashboard/medicalcen')
                else:
                    messages.error(request, "Login not permitted")
                    logout(request)
            else:
                messages.error(request, "Incorrect Credentials")
    return render(request, 'login-medicalcen.html')