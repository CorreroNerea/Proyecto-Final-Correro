from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
    


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
            return render(request,"usersapp/login.html")
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
            if miFormulario.cleaned_data.get('imagen'): 
                if Imagen.objects.filter(user=usuario).exists():  
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()  
                else:
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()  

            miFormulario.save()  

            return render(request, "usersapp/login.html")  

    else:  
        miFormulario = UserEditForm(instance=usuario) 

    return render(request, "usersapp/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


#Mariano extraterrestre123
#Pablo qwe784512
#Palmiere monoestrella52