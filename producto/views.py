from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages
from django.http import HttpResponseRedirect

def productos(request):
    productosLista = Producto.objects.all()
    messages.success(request, '¡Productos Listados!')
    return render(request, 'producto/gestionProductos.html', {"productos": productosLista })

def registrarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    stock = request.POST['txtStock']
    
    producto = Producto.objects.create(
        codigo=codigo, nombre=nombre, precio=precio, stock_unidades=stock
    )
    messages.success(request, 'El Producto fue Registrado!')
    return redirect('producto')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    return render(request, "producto/edicionProducto.html", {"producto": producto})

def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    stock = request.POST['txtStock']

    producto = Producto.objects.get(codigo = codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.stock_unidades = stock
    producto.save()

    messages.success(request, 'El Producto fué modificado!')
    return redirect('producto')
    
def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo = codigo)
    producto.delete()

    messages.success(request, 'El Producto fué Eliminado!')

    return redirect('producto')
