from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    password = forms.CharField(max_length=12)
    num_cliente = forms.IntegerField()
    email = forms.EmailField()
    
class SupervisorFormulario(forms.Form):
    nombre_emp = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    #permiso = forms.CharField(max_length=50) 
    
class PedidoFormulario(forms.Form):
    codigo_ped = forms.CharField(max_length=8)
    aprobado = forms.BooleanField()
    fecha_de_entrega = forms.DateField()
    
class ProductoFormulario(forms.Form):
    codigo_prod = forms.CharField(max_length=8)
    producto = forms.CharField(max_length=40)