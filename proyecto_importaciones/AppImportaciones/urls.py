from django.urls import path
from . import views
from .views import  ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, ProductoListView, CompraListView, CompraDetailView, ComprarListView, PermisoDetail



urlpatterns = [
    path('', views.index, name='inicio'),
    # path('/<int:pk>/', views.PerfilDetail, name='Permiso'),

    
    #Pedidos
    path('pedido/', views.pedido, name='pedidos'),
    path('form_pedido/', views.pedidoFormulario, name='formpedido'),
    
 
    #Busqueda
    path('form_busqueda_prod/', views.busqueda, name='buscar_prod'), 
    path('form_busqueda_prod2/', views.buscar, name='buscar'),
    
    
    #Productos Administradores
    path('producto/<int:pk>/', ProductoListView.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', ProductoDetailView.as_view(), name='articulo-detail'),
    path('articulo/create/', ProductoCreateView.as_view(), name='articulo-create'),
    path('articulo/<int:pk>/editar/', ProductoUpdateView.as_view(), name='articulo-update'),
    path('articulo/<int:pk>/borrar/', ProductoDeleteView.as_view(), name='articulo-delete'),
    path('upload/<int:pk>/editar/', views.upload_image_prod, name='upload_image'),

    
    path('permiso/<int:pk>/', views.PermisoDetail, name='permiso'),   #--> Permisos
    
    
    #About
    path('about', views.about, name="About"),

    
    #Compra
    path('compraList/', CompraListView.as_view(), name='compra-list'),
    path('compraList/', CompraListView.as_view(), name='compra-list'),
    path('compraarticulo/<int:pk>/', CompraDetailView.as_view(), name='compra-detail'),
    path('agregar/<int:pk>/', views.agregar, name='compra-agregar'),
     
        
    #BusquedaCompra --> para buscar prod desde pagina cliente
    path('form_busqueda_prod_compra/', views.busquedaCompra, name='buscar_prod_compra'), 
    
    
    #Carrito
    path('carritoList/', ComprarListView.as_view(), name='carrito-list'),
    path('finalizado/', views.comprar, name='Finalizado'),
    
   
]