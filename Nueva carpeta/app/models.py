from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Productos(models.Model):
    id=models.IntegerField(primary_key=True)
    Nombre=models.CharField(max_length=100)
    Presentacion=models.CharField(max_length=30)
    Fecha=models.DateField()
    Cantidad=models.IntegerField()
    
    class meta:
       db_table='Productos'
       
class CambioStock(models.Model):
    id_cambio=models.AutoField(primary_key=True)
    id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    tipo_cambio=models.CharField(max_length=20)
    comentario=models.CharField(max_length=100)
    fecha_c=models.DateField()
    
    class meta:
        db_table='CambioStock'       
        


