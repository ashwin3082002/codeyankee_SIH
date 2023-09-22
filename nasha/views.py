from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from database.models import user_roles

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            search_details = user_roles.objects.filter(username=username)
            if search_details[0].role == "admin":
                login(request, user)
                return redirect('hospital_dashboard')
            elif search_details[0].role == "gov":
                login(request, user)
                return redirect('gov_dashboard')
            elif search_details[0].role == "patient":
                login(request, user)
                return redirect('patient_dashboard')
            # login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == "1":
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user_role_obj = user_roles(username=username, role="gov")
            user_role_obj.save()

        elif role == "2":
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user_role_obj = user_roles(username=username, role="admin")
            user_role_obj.save()
        
        elif role == "3":
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user_role_obj = user_roles(username=username, role="patient")
            user_role_obj.save()

            
        messages.success(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'register.html')


def testing(request):
    return render(request, 'gov/heatmap.html')