from django.shortcuts import render, redirect
from AppImportaciones.forms import ClienteFormulario, SupervisorFormulario, PedidoFormulario, ProductoFormulario, ImgProductoFormulario
from AppImportaciones.models import Cliente, Supervisor, Pedido, Producto, Compra 
from django.views.generic import  DetailView, CreateView, UpdateView, DeleteView , ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'appImportacion/inicio.html') 

def index(request):
    ahora =  datetime.now().strftime("%d/%m/%y, %H:%M:%S")
    return render(request, 'appImportacion/inicio.html', {'ahora': ahora})


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


def PermisoDetail(request, pk):
    user = get_object_or_404(User, pk=pk)

    productos = Producto.objects.all()  

    context = {
        'user': user,
        'is_staff': request.user.is_staff,
        'productos': productos
    }
    
    return render(request, 'appImportacion/producto_list.html', context)         

          
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'appImportacion/producto_detail.html'

class ProductoCreateView(LoginRequiredMixin, CreateView): 
    model = Producto
    template_name = 'appImportacion/producto_create.html'
    fields = ['codigo_prod', 'producto', 'precio', 'descripcion', 'imagen']
    success_url = reverse_lazy('inicio')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):  
    model = Producto
    template_name = 'appImportacion/producto_update.html'
    fields = ['codigo_prod', 'producto', 'precio', 'descripcion' ]
    success_url = reverse_lazy('articulo-list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'appImportacion/producto_confirm_delete.html'
    success_url = reverse_lazy('inicio')

@login_required
def upload_image_prod(request, pk):
    imagen = None  #  UnboundLocalError --> variable no def, definir

    if request.method == 'POST':
        form = ImgProductoFormulario(request.POST, request.FILES)

        if form.is_valid():
            imagen = form.cleaned_data.get('imagen') 

            if imagen: #si por POST traemos imagen
                producto = get_object_or_404(Producto, pk=pk) #traer el obj existente a updetear

                if producto.imagen: #si tiene imagen
                    producto.imagen.imagen = imagen # updetear
                    producto.imagen.save() #save
                else:
                    producto.imagen = imagen
                    producto.save()

            return render(request, "appImportacion/inicio.html")

    else:
        form = ImgProductoFormulario()  

    return render(request, "appImportacion/edita_images.html", {"form": form, "imagen": imagen})   
    
# -------------- About Me ---------------
def about(request):
       return render(request, 'appImportacion/About.html')

# ---------------- Busqueda ---------
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
        

# --------------- Busqueda Compra ---------------------
def busquedaCompra(request):
    return render(request, 'appImportacion/BusquedaProdCompra.html')

#--------------- Compra ----------------------
class CompraListView(LoginRequiredMixin, ListView):
     model = Producto
     template_name = 'appImportacion/compra_list.html'
     context_object_name = 'productos' 

@login_required     
def agregar(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    
    compra = Compra(
        codigo_prod = producto.codigo_prod,
        producto=producto.producto,
        cantidad=1,
        precio=producto.precio
    )
    compra.save()
    
    messages.success(request, f"Producto '{producto.producto}' agregado a carrito de compra.")
    
    return redirect('compra-list')


class CompraDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'appImportacion/compra_detail.html'
    

# ----------- Carrito ----------------------  
  
class ComprarListView(LoginRequiredMixin, ListView):
     model = Compra
     template_name = 'appImportacion/lista_comprar.html'
     context_object_name = 'productos' 
 
@login_required    
def comprar(request):
    if Compra.objects.exists():
        Compra.objects.all().delete()
        return render(request, 'appImportacion/success.html')
    else:
        print("No hay items en su carrito de compra")
    
    return render(request, 'appImportacion/empty.html')
