from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    password = models.CharField(max_length=12)
    num_cliente = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
     return f"Nombre: {self.nombre}, Numero cliente: {self.num_cliente}, Email: {self.email} "

class Supervisor(models.Model):
    nombre_emp = models.CharField(max_length=40)
    numero = models.IntegerField()

class Pedido(models.Model):
    codigo_ped = models.CharField(max_length=8)
    aprobado = models.BooleanField()
    fecha_de_entrega = models.DateField()
    
    def __str__(self):
     return f"Codigo Pedido: {self.codigo_ped}, Estatus: {self.aprobado}, Fecha de entrega: {self.fecha_de_entrega} "


#----------Productos-----------     
class Producto(models.Model):
    codigo_prod = models.CharField(max_length=8)
    producto = models.CharField(max_length=40)
    precio = models.IntegerField(default=100)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='media/') 

    def __str__(self):
        return f"Codigo Producto: {self.codigo_prod}, Producto: {self.producto}"
    
    
#----------Compra----------- 
class Compra(models.Model):
    codigo_prod = models.CharField(max_length=8)
    producto = models.CharField(max_length=40)
    precio = models.IntegerField(default=100)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Codigo Producto: {self.codigo_prod}, Producto: {self.producto}, Precio: {self.precio}, cantidad: {self.cantidad}, fecha de compra: {self.fecha_compra}"