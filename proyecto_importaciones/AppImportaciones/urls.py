from django.urls import path
from . import views
from .views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    #Cliente
    path('', views.index, name='inicio'),
    path('cliente/', views.cliente, name='clientes'),
    path('form_cliente/', views.clienteFormulario, name='formcliente'),
    
    
    #Supervisor
    path('superv/', views.supervisor, name='superv'),
    path('form_supervisor/', views.supervFormulario, name='formsupervisor'),
    
    
    #Pedidos
    path('pedido/', views.pedido, name='pedidos'),
    path('form_pedido/', views.pedidoFormulario, name='formpedido'),
    
 
    #Busqueda
    path('form_busqueda_prod/', views.busqueda, name='buscar_prod'), 
    path('form_busqueda_prod2/', views.buscar, name='buscar'),
    
    #Productos
    path('prod/', views.producto, name='productos'),
    #path('form_prod/', views.productoFormulario, name='formprod'),
    #CRUD
    path('prod/', ProductoListView.as_view(), name='articulo-list'),
    path('articulo/<int:codigo_prod>/', ProductoDetailView.as_view(), name='articulo-detail'),
    path('articulo/create/', ProductoCreateView.as_view(), name='articulo-create'),
    path('articulo/<int:codigo_prod>/editar/', ProductoUpdateView.as_view(), name='articulo-update'),
    path('articulo/<int:codigo_prod>/borrar/', ProductoDeleteView.as_view(), name='articulo-delete'),
]