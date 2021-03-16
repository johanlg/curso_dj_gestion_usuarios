# Importaciones de Django   ########################################################
from django.shortcuts           import render
from django.core.mail           import send_mail
from django.urls                import reverse_lazy ,reverse
from django.contrib.auth        import authenticate ,login   ,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http                import HttpResponseRedirect

from django.views.generic import(
    View
)

from django.views.generic.edit import(
    FormView
)


# Importaciones propias     ########################################################
from .forms import (
    UserRegisterForm        ,
    UserLoginForm           ,
    UserUpdatePasswordForm  ,
    VerificationUserForm
)

from .models import User

from .functions import generador_codigo_validacion_email_login


# Create your views here.   ########################################################

class UserRegisterView(FormView):                       #   ---------------------------    Vista Registro de Usuario
    template_name = 'users/register.html'
    form_class    = UserRegisterForm

    def form_valid(self, form):

        # Generamos el codigo para validar el email del usuario registrado
        codigo_validacion = generador_codigo_validacion_email_login()

        username  = form.cleaned_data['username'] 
        email     = form.cleaned_data['email']    
        password1 = form.cleaned_data['password1']
        nombres   = form.cleaned_data['nombres']  
        apellidos = form.cleaned_data['apellidos']
        genero    = form.cleaned_data['genero']   

        usuario = User.objects.create_user(
            username                        ,
            email                           ,
            password1                       ,
            nombres      = nombres          ,
            apellidos    = apellidos        ,
            genero       = genero           ,
            codeRegistro = codigo_validacion,

        )
        # Enviar el codigo al email del usuario nuevo
        # 1) Datos de envio de email
        asunto          = 'Confirmacion de email'
        mensaje         = 'Codigo de verificacion: ' + codigo_validacion
        email_remitente = 'johanlg2506@gmail.com'
        
        # 2) Envio email
        send_mail(asunto, mensaje, email_remitente, [email,])
        
        # 3) Redirigir a pantalla de validacion        
        return HttpResponseRedirect(
            reverse(
            'users_app:verificationUser',
            kwargs={'pk':usuario.id}
            )
        )


class VerificationUserView(FormView):
    template_name = 'users/verification-user.html'
    form_class    = VerificationUserForm
    success_url   = reverse_lazy('users_app:userLogin')

    def get_form_kwargs(self):
        kwargs = super(VerificationUserView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        User.objects.filter(
            id=self.kwargs['pk'],
        ).update(
            is_active=True
        )
        return super(VerificationUserView, self).form_valid(form)

class UserLoginView(FormView):                              #   --------------------------    Vista Login de Usuario
    template_name = 'users/login.html'
    form_class    = UserLoginForm
    success_url   = reverse_lazy('home_app:homePage')

    def form_valid(self, form):
        username_recibido = form.cleaned_data['username']
        password_recibido = form.cleaned_data['password']

        user = authenticate(
            username = username_recibido,
            password = password_recibido
        )

        login(self.request, user)

        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(View):                                 #   -------------------------    Vista Logout de Usuario

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse('users_app:userLogin')
        )
        

class UserUpdatePasswordView(LoginRequiredMixin,FormView):  #   --------------------    Vista Actualizacion Password
    template_name = 'users/user-update-password.html'
    form_class    = UserUpdatePasswordForm
    success_url   = reverse_lazy('users_app:userLogin')
    login_url     = reverse_lazy('users_app:userLogin')

    def form_valid(self, form):
        
        usuario_activo    = self.request.user               # Recuperamos el usuario que esta activo actualmente
        password_actual   = form.cleaned_data['password1']  # Recuperamos la pass actual del usuario activo

        # Intentamos autenticarnos con las credenciales actuales
        user = authenticate(
            username = usuario_activo.username,
            password = password_actual
        )

        # Validamos si se pudo atenticar las credenciales
        if user :
            password_nueva = form.cleaned_data['password2'] # Recuperamos la nueva password
            usuario_activo.set_password(password_nueva)     # Guardamos la nueva password
            usuario_activo.save()                           # Guardamos cambios
            logout(self.request)
        
            
        return super(UserUpdatePasswordView, self).form_valid(form)





