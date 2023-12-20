from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50) 
    precio=models.PositiveIntegerField()
    stock_unidades=models.PositiveIntegerField()   
    
    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.nombre, self.codigo)