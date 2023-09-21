from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("", views.land, name="land"),
    
    # path('medicalcen',views.medicalcen),
]