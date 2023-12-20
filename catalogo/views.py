from django.shortcuts import render
from .models import Categoria_1

def catalogo(request):
    categorias_1 = Categoria_1.objects.all()
    return render(request, "catalogo/catalogo.html", {'categorias_1':categorias_1})

   
