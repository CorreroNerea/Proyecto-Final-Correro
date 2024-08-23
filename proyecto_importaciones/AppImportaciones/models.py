from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    password = models.CharField(max_length=12)
    num_cliente = models.IntegerField()
    email = models.EmailField()
    
class Supervisor(models.Model):
    nombre_emp = models.CharField(max_length=40)
    numero = models.IntegerField()
   # permiso = models.CharField(max_length=50)

class Pedido(models.Model):
    codigo_ped = models.CharField(max_length=8)
    aprobado = models.BooleanField()
    fecha_de_entrega = models.DateField()
     
class Producto(models.Model):
    codigo_prod = models.CharField(max_length=8)
    producto = models.CharField(max_length=40)
