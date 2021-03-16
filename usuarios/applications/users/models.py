from django.db import models

# Create your models here.
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino') ,
        ('O', 'Otros')
    )
    
    # Campos propios
    username     = models.CharField(max_length=10, unique=True)
    email        = models.EmailField()
    nombres      = models.CharField(max_length=30, blank=True)
    apellidos    = models.CharField(max_length=30, blank=True)
    genero       = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    codeRegistro = models.CharField(max_length=6)

    # Campos del AbstractBaseUser
    is_staff  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
    