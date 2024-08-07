from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path("", views.acceuil , name = "acceuil"),
    path("", views.connexion , name = "connexion"),
    path("", views.inscription , name = "inscription"),
]
