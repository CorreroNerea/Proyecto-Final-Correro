from django.shortcuts import render
from AppImportaciones.forms import ClienteFormulario, SupervisorFormulario, PedidoFormulario, ProductoFormulario
from AppImportaciones.models import Cliente, Supervisor, Pedido, Producto
from django.http import HttpResponse


def index(request):
    return render(request, 'appImportacion/inicio.html') 

#Cliente -----------
def cliente(request):
    return render(request, 'appImportacion/cliente.html')

def clienteFormulario(request):
    if request.method == "POST": 
        miFormulario = ClienteFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            cliente = Cliente(nombre=informacion["nombre"], password=informacion["password"], num_cliente=informacion["num_cliente"], email=informacion["email"]) 
            cliente.save()  
            return render(request, "appImportacion/index.html")  
    else:
        miFormulario = ClienteFormulario()  
        
    return render(request, "appImportacion/clienteFormulario.html", {"miFormulario": miFormulario})


#Supervisor -----------
def supervisor(request):
    return render(request, 'appImportacion/supervisor.html')

def supervFormulario(request):
    if request.method == "POST": 
        miFormulario = SupervisorFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            supervisor = Supervisor(nombre_emp=informacion["nombre_emp"], numero=informacion["numero"]) 
            supervisor.save()  
            return render(request, "appImportacion/index.html")  
    else:
        miFormulario = SupervisorFormulario()  
        
    return render(request, "appImportacion/supervisorFormulario.html", {"miFormulario": miFormulario})


#Pedido ---------------
def pedido(request):
    return render(request, 'appImportacion/pedido.html')

def pedidoFormulario(request):
    if request.method == "POST": 
        miFormulario = PedidoFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            pedido = Pedido(codigo_ped=informacion["codigo_ped"], aprobado=informacion["aprobado"], fecha_de_entrega=informacion["fecha_de_entrega"]) 
            pedido.save()  
            return render(request, "appImportacion/index.html")  
    else:
        miFormulario = PedidoFormulario()  
        
    return render(request, "appImportacion/pedidoFormulario.html", {"miFormulario": miFormulario})


#Productos---------------
def producto(request):
    return render(request, 'appImportacion/producto.html')

#producto = Producto(codigo_prod = 2253, producto = "Sticker_totoro") #Clase 18 --> revisar
#producto.save()

def productoFormulario(request):
    if request.method == "POST": 
        miFormulario = ProductoFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            productos = Producto(codigo_prod=informacion["codigo_prod"], producto=informacion["producto"]) 
            productos.save()  
            return render(request, "appImportacion/index.html")  
    else:
        miFormulario = ProductoFormulario()  
        
    return render(request, "appImportacion/prodFormulario.html", {"miFormulario": miFormulario})


#Busqueda ---------
def busqueda(request):
    return render(request, 'appImportacion/BusquedaProd.html')
   

def buscar(request):
    if request.GET["codigo_prod"]:
        codigo_prod = request.GET["codigo_prod"]
        producto = Producto.objects.filter(codigo_prod__icontains=codigo_prod)
        
        return render(request, "appImportacion/resultado_prod.html", {"producto": producto, "codigo_prod": codigo_prod})
    
    else:
        respuesta = "El producto no se encuentra o los datos son incorrectos"
        
    return HttpResponse(respuesta)
        
   

