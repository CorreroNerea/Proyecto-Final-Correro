from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('cliente/', views.cliente, name='clientes'),
    path('superv/', views.supervisor, name='superv'),
    path('pedido/', views.pedido, name='pedidos'),
    path('prod/', views.producto, name='productos'),
    path('form_cliente/', views.clienteFormulario, name='formcliente'),
    path('form_supervisor/', views.supervFormulario, name='formsupervisor'),
    path('form_pedido/', views.pedidoFormulario, name='formpedido'),
    path('form_prod/', views.productoFormulario, name='formprod'),
    path('form_busqueda_prod/', views.busqueda, name='buscar_prod'), 
    path('form_busqueda_prod2/', views.buscar, name='buscar'),
]