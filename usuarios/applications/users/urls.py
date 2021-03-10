from django.contrib import admin
from django.urls    import path

from . import views

name_app = 'users_app'

urlpatterns = [

    path('user-register/', views.UserRegisterView.as_view() , name='userRegister'),
    path('user-login/'   , views.UserLogin.as_view()        , name='userLogin'   ),
    path('user-logout/'  , views.UserLogout.as_view()       , name='userLogout'  ),

]