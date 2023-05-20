from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from streamz.models import comentarios,Video
from django.forms import ModelChoiceField

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirmación de contraseña',widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = {'username','email','password1','password2'}
#         help_text = {k:"" for k in fields}

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control rounded'}))
    username = forms.CharField(label='Usuario',max_length=24,widget=forms.TextInput(attrs={'class': 'form-control rounded'}))
    password1 = forms.CharField(label='Contraseña',max_length=16,widget=forms.PasswordInput(attrs={'class': 'form-control rounded'}))
    password2 = forms.CharField(label='Confirmación de contraseña',max_length=16,widget=forms.PasswordInput(attrs={'class': 'form-control rounded'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.from_class = 'form-horizontal'

        self.helper.layout = Layout(
            Row(
                Column('email', css_class='col-md-6 rounded'),
                Column('username', css_class='col-md-6'),
                css_class='form-group'
            ),
            Row(
                Column('password1', css_class='col-md-6'),
                Column('password2', css_class='col-md-6'),
                css_class='form-group'
            ),
            Submit('submit', 'Registrarse', css_class='btn btn-primary')
        )            

class guardarVideoForm(forms.Form):
   # imagen = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_enctype = 'multipart/form-data' 

        self.helper.layout = Layout(
            # Row(
            #     Column('imagen', css_class='col-md-6'),
            #     css_class='form-group'
            # ),
            Submit('submit', 'Guardar video', css_class='btn btn-primary')
        )

class guardarComentario(forms.Form):
    # username = forms.CharField(max_length=50)
    comentario = forms.CharField(max_length=280,widget=forms.TextInput(attrs={'class': 'form-control rounded'}))
    # id_video = ModelChoiceField(queryset=Video.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_enctype = 'multipart/form-data' 

        self.helper.layout = Layout(
            Row(
                Column('comentario', css_class='col-md-6'),
                css_class='form-group'
            ),
            Submit('submit', 'Envíar', css_class='btn btn-primary')
        )