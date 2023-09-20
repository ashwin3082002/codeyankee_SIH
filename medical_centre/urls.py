from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard", views.hosp_dash, name="hospital_dashboard"),
    path("patient/add", views.patient_add, name="patient_create"),
]