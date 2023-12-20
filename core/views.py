from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    return render(request, "core/contacto.html")


