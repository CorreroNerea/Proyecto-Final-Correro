from django.shortcuts import render
from AppImportaciones.forms import ClienteFormulario, SupervisorFormulario, PedidoFormulario
from AppImportaciones.models import Cliente, Supervisor, Pedido, Producto
from django.views.generic import  DetailView, CreateView, UpdateView, DeleteView , ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
@login_required
def supervisor(request):
    return render(request, 'appImportacion/supervisor.html')

@login_required
def supervFormulario(request):
    if request.method == "POST": 
        miFormulario = SupervisorFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            supervisor = Supervisor(nombre_emp=informacion["nombre_emp"], numero=informacion["numero"]) 
            supervisor.save()  
            return render(request, "appImportacion/inicio.html")  
    else:
        miFormulario = SupervisorFormulario()  
        
    return render(request, "appImportacion/supervisorFormulario.html", {"miFormulario": miFormulario})


#Pedido ---------------
@login_required
def pedido(request):
    return render(request, 'appImportacion/pedido.html')

@login_required
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
class ProductoListView(ListView):
     model = Producto
     template_name = 'appImportacion/producto_list.html'
     context_object_name = 'productos'        
          
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'appImportacion/producto_detail.html'

class ProductoCreateView(LoginRequiredMixin, CreateView): 
    model = Producto
    template_name = 'appImportacion/producto_create.html'
    fields = ['codigo_prod', 'producto']
    success_url = reverse_lazy('articulo-list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):  
    model = Producto
    template_name = 'appImportacion/producto_update.html'
    fields = ['codigo_prod', 'producto']
    success_url = reverse_lazy('articulo-list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'appImportacion/producto_confirm_delete.html'
    success_url = reverse_lazy('articulo-list')
    
    

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
        
   

#Mariano extraterrestre123