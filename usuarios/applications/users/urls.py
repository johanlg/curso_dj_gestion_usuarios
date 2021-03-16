from django.contrib import admin
from django.urls    import path

from . import views

name_app = 'users_app'

urlpatterns = [

    path('user-register/'          ,views.UserRegisterView.as_view()       ,name='userRegister'      ),
    path('user-login/'             ,views.UserLoginView.as_view()          ,name='userLogin'         ),
    path('user-logout/'            ,views.UserLogoutView.as_view()         ,name='userLogout'        ),
    path('user-update-password/'   ,views.UserUpdatePasswordView.as_view() ,name='userUpdatePassword'),
    path('verification-user/<pk>/' ,views.VerificationUserView.as_view()   ,name='verificationUser'  ),

]