from django.urls import path
from . import views
from .views import  ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, ProductoListView


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
    path('producto/', ProductoListView.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', ProductoDetailView.as_view(), name='articulo-detail'),
    path('articulo/create/', ProductoCreateView.as_view(), name='articulo-create'),
    path('articulo/<int:pk>/editar/', ProductoUpdateView.as_view(), name='articulo-update'),
    path('articulo/<int:pk>/borrar/', ProductoDeleteView.as_view(), name='articulo-delete'),
]