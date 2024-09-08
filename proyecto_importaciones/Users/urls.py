from django.urls import path
from Users import views

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', views.redirect, name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"), 
    path('cambiar_pass/', views.CambiarContrasenia, name="CambiarPass"),
    
    # -------------- Perfil -------------------- 
    path('perfil/<int:pk>/', views.PerfilDetail, name='Perfil'),
    
]