from django.contrib import admin
from AppImportaciones.models import Cliente, Supervisor, Pedido, Producto


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Supervisor)
admin.site.register(Pedido)
admin.site.register(Producto)