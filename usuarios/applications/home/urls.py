from django.contrib import admin
from django.urls    import path

from . import views

name_app='home_app'

urlpatterns = [

    path('home-page/',views.HomePage.as_view(),name='homePage'),

]