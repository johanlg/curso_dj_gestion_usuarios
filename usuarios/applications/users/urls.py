from django.contrib import admin
from django.urls    import path

from . import views

name_app = 'users_app'

urlpatterns = [

    path('user-register/', views.UserRegisterView.as_view(), name='userRegister'),

]