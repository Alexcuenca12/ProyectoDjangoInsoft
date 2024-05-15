from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

from P_persona.models import en_persona

# Create your models here.

""""
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, unique=False)
    identification_card = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)



    class Meta:
       # unique_together = (('email', 'company_key'))
        db_table = 'usuario'
        
        
        __________________





class ADUsuario(AbstractUser):


    cod_usuario = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=60)
    pw_app = models.CharField(max_length=30, blank=True, null=True)
    pw_bd = models.CharField(max_length=30, blank=True, null=True)
    cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE)

    class Meta:
        db_table = 'AD_USUARIO'




"""
