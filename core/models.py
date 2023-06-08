from django.db import models

# Create your models here.

# TABLA TIPO PRODUCTO
class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

# TABLA PRODUCTO
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)
    vencimiento = models.DateField()
    imagen = models.ImageField(null=True,blank=True)
    vigente = models.BooleanField()

    def __str__(self):
        return self.nombre

