from django.shortcuts import render

# Create your views here.

def dash(request):
    return render(request, 'gov/dash.html')

def heatmap(request):
    return render(request, 'gov/heatmap.html')
