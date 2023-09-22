
from django.urls import path
from . import views


urlpatterns = [
    path("dashboard", views.dash, name="patient_dashboard"),
    
    # path('medicalcen',views.medicalcen),
]