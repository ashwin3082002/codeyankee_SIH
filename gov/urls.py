
from django.urls import path
from . import views


urlpatterns = [
    path("dashboard", views.dash, name="gov_dashboard"),
]