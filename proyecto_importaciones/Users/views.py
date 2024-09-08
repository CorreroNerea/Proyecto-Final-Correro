from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import Imagen, User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
    

# ------------- Cuenta -----------------
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "appImportacion/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "usersapp/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            return render(request,"appImportacion/inicio.html")
        else:
            # Mostrar los errores del formulario
            msg_register = form.errors.as_text()
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"usersapp/registro.html" ,  {"form":form, "msg_register": msg_register})


   # Vista de editar el perfil

@login_required
def editar_perfil(request):
    usuario = request.user  
    
    if request.method == 'POST':  
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid(): 
            miFormulario.save() #

            imagen = miFormulario.cleaned_data.get('imagen') #
            if imagen:
                # Verifica si ya tiene imagen de perfil
                if Imagen.objects.filter(user=usuario).exists():  
                    # Si ya existe, actualizar la imagen
                    usuario.imagen.imagen = imagen
                    usuario.imagen.save()  
                else:
                    # Si no existe, crear una nueva instancia de Imagen
                    avatar = Imagen(user=usuario, imagen=imagen)
                    avatar.save()  

            return render(request, "appImportacion/inicio.html")  
    else:  
        miFormulario = UserEditForm(instance=usuario) 

    return render(request, "usersapp/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})

@login_required
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "usersapp/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")
  
@login_required
def redirect(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'appImportacion/inicio.html') 
    return render(request, 'appImportacion/inicio.html')
     
# -------------- Perfil --------------------   
def PerfilDetail(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    return render (request, 'usersapp/perfil_list.html', {'user': user})

