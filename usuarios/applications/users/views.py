from django.shortcuts import render

from django.views.generic.edit import(
    FormView
)

from .forms import UserRegisterForm

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