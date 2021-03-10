from django.shortcuts    import render
from django.urls         import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http         import HttpResponseRedirect

from django.views.generic import(
    View
)

from django.views.generic.edit import(
    FormView
)

from .forms import (
    UserRegisterForm,
    UserLoginForm
)

from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class    = UserRegisterForm
    success_url   = '.'

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

