from django.db import models

class Categoria_1(models.Model):
    titulo = models.CharField(max_length=100, verbose_name= "Título")
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(verbose_name= "Imagen", upload_to= 'categoria_1')
    
    def __str__(self) -> str:
        return self.titulo