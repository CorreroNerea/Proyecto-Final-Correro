from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}
        


class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Ingrese su email:")
    password1 = None
    password2 = None
    # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username",'email']
        help_texts = {k:"" for k in fields}