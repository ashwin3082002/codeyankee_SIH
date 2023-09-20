from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def testing(request):
    return render(request, 'register.html')