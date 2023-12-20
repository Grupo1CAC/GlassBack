"""
URL configuration for back_glass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from catalogo import views as catalogo_views
from producto import views as producto_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('contacto', core_views.contacto, name="contacto"),
    path('catalogo', catalogo_views.catalogo, name="catalogo"),
    path('nosotros', core_views.nosotros, name="nosotros"),
    path('producto', producto_views.productos, name="producto"),
    path('registrarProducto/', producto_views.registrarProducto),
    path('edicionProducto/<codigo>',producto_views.edicionProducto),
    path('editarProducto/', producto_views.editarProducto), 
    path('eliminarProducto/<codigo>',producto_views.eliminarProducto),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
