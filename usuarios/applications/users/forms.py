from django              import forms
from django.contrib.auth import authenticate
from .models             import User


class UserRegisterForm(forms.ModelForm):    #   Formulario para registrar usuarios  --------------------------------

    password1 = forms.CharField(
        
        label    = 'Contraseña1' ,
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Ingrese contraseña',
                'class'       : 'form-control'
            }
        ),
    )


    password2 = forms.CharField(
        
        label    = 'Contraseña2' ,
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Repetir contraseña',
                'class'       : 'form-control'
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


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder' : 'Username' , 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder'    : 'Email'    , 'class': 'form-control'})
        self.fields['nombres'].widget.attrs.update({'placeholder'  : 'Nombres'  , 'class': 'form-control'})
        self.fields['apellidos'].widget.attrs.update({'placeholder': 'Apellidos', 'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-select'})
        

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        cantidad_minima_caracteres = 5

        if password1 != password2:
            self.add_error('password1', 'Las contraseñas no coinciden')

        elif len(password1) < cantidad_minima_caracteres:
            self.add_error('password1', 'La contraseña debe tener minimo 5 caracteres')


class VerificationUserForm(forms.Form):     #   Formulario para validar registro usuarios  -------------------------
    codeRegistro = forms.CharField(
        required   = True ,
        max_length = 6    ,
        widget     = forms.TextInput(
            attrs = {
                'placeholder' : 'Ingrese codigo de verificacion',
                'class'       : 'form-control'
            }
        ),
    )

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationUserForm, self).__init__(*args, **kwargs)
    
    
    def clean_codeRegistro(self):
        codigo = self.cleaned_data['codeRegistro']

        if len(codigo) == 6:
            activo = User.objects.code_validation(
                self.id_user,
                codigo
            )

            if not activo:
                raise forms.ValidationError({'codeRegistro':'El codigo es incorrecto'})    
        else:
            raise forms.ValidationError({'codeRegistro':'El codigo es incorrecto'})


class UserLoginForm(forms.Form):            #   Formulario para iniciar sesion usuarios  ---------------------------

    username = forms.CharField(
        
        required = True,
        widget   = forms.TextInput(
            attrs = {
                'placeholder' : 'Username',
                'class'       : 'form-control'
            }
        ),
    )

    password = forms.CharField(
        
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Contraseña',
                'class'       : 'form-control'
            }
        ),
    )


    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()

        username_recibido = self.cleaned_data['username']
        password_recibido = self.cleaned_data['password']

        user = authenticate(
            username = username_recibido,
            password = password_recibido
        )

        if not user:
            raise forms.ValidationError({'username':'Los datos de usuario no son correctos'})

        return self.cleaned_data


class UserUpdatePasswordForm(forms.Form):   #   Formulario para actualizar password usuarios  ----------------------

    password1 = forms.CharField(
        
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Contraseña actual',
                'class'       : 'form-control'
            }
        ),
    )

    password2 = forms.CharField(
        
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Contraseña nueva',
                'class'       : 'form-control'
            }
        ),
    )

    password3 = forms.CharField(
        
        required = True         ,
        widget   = forms.PasswordInput(
            attrs = {
                'placeholder' : 'Confirma contraseña nueva',
                'class'       : 'form-control'
            }
        ),
    )


    def clean(self):
        cleaned_data = super(UserUpdatePasswordForm, self).clean()

        password_actual = self.cleaned_data['password1']  # Recuperamos la contraseña actual que ingreso el usuario activo

        password_nueva               = self.cleaned_data['password2']   # Recuperamos password nueva
        password_nueva_confirmacion  = self.cleaned_data['password3']   # Recuperamos confirmacion password nueva

        cantidad_minima_caracteres = 5

        if password_nueva != password_nueva_confirmacion:
            self.add_error('password3', 'Las contraseñas no coinciden')
        elif len(password_nueva) < cantidad_minima_caracteres:
            self.add_error('password3', 'La contraseña debe tener minimo 5 caracteres')


        return self.cleaned_data


