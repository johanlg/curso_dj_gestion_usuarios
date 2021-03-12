from django.shortcuts           import render
from django.urls                import reverse_lazy, reverse
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http                import HttpResponseRedirect

from django.views.generic import(
    View
)

from django.views.generic.edit import(
    FormView
)

from .forms import (
    UserRegisterForm,
    UserLoginForm   ,
    UserUpdatePasswordForm
)

from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class    = UserRegisterForm
    success_url   = 'users_app:userLogin'

    def form_valid(self, form):

        username  = form.cleaned_data['username'] 
        email     = form.cleaned_data['email']    
        password1 = form.cleaned_data['password1']
        nombres   = form.cleaned_data['nombres']  
        apellidos = form.cleaned_data['apellidos']
        genero    = form.cleaned_data['genero']   

        User.objects.create_user(
            username                ,
            email                   ,
            password1               ,
            nombres   = nombres     ,
            apellidos = apellidos   ,
            genero    = genero      ,

        )

        return super(UserRegisterView, self).form_valid(form)


class UserLogin(FormView):
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

        return super(UserLogin, self).form_valid(form)


class UserLogout(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse('users_app:userLogin')
        )

class UserUpdatePassword(LoginRequiredMixin,FormView):
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
        
            


        return super(UserUpdatePassword, self).form_valid(form)





