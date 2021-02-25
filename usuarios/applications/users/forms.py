from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        
        label    = 'Contraseña' ,
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Ingrese contraseña'
            }
        ),
    )


    password2 = forms.CharField(
        
        label    = 'Contraseña' ,
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Repetir contraseña'
            }
        ),
    )


    class Meta:
        model  = User
        fields = (
            'username'  ,
            'email'     ,
            'nombres'   ,
            'apellidos' ,
            'genero'    ,
        )

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        cantidad_minima_caracteres = 5

        if password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')

        if len(password1) < cantidad_minima_caracteres:
            self.add_error('password1', 'La contraseña debe tener minimo 5 caracteres')
        

