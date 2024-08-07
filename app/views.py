from django.shortcuts import render
from django.shortcuts import redirect



def acceuil (request) :
    return render (request , "acceuil.html")

def connexion (request) :
    return render (request , "connexion.html")

def inscription (request) :
    return render (request , "inscription.html")
    

# Create your views here.
