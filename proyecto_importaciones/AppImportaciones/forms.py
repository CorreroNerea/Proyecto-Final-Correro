from django import forms
from .models import Producto

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    password = forms.CharField(max_length=12)
    num_cliente = forms.IntegerField()
    email = forms.EmailField()
    
class SupervisorFormulario(forms.Form):
    nombre_emp = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    
class PedidoFormulario(forms.Form):
    codigo_ped = forms.CharField(max_length=8)
    aprobado = forms.BooleanField()
    fecha_de_entrega = forms.DateField()
    
class ProductoFormulario(forms.Form):
    codigo_prod = forms.CharField(max_length=8)
    producto = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    descripcion = forms.CharField(max_length=500)
    #imagen = forms.ImageField(label="images", required=False)
    
    # class Meta:
    #     model = Producto
    #     fields = ['images']
 
class ImgProductoFormulario(forms.Form):
    imagen = forms.ImageField(label="imagen")