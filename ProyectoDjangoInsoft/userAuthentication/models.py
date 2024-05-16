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




"""
class ADUsuario(AbstractUser):

    # Anula los campos que no necesitas

    first_name = None
    last_name = None
    email = None

    cod_usuario = models.CharField(max_length=30, primary_key=True ,  verbose_name="COD_USUARIO")
    nombre = models.CharField(max_length=60, verbose_name="NOMBRE")
    pw_app = models.CharField(max_length=30, blank=True, null=True, verbose_name="PW_APP")
    pw_bd = models.CharField(max_length=30, blank=True, null=True, verbose_name="PW_DB")
   # cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE,  verbose_name="COD_PERSONA")


    class Meta:
        db_table = 'AD_USUARIO'



class ADUSUARIOEMPRESA(models.Model):
    COD_EMPRESA = models.CharField(max_length=8,  verbose_name="COD_EMPRESA")
    estado = models.IntegerField(verbose_name="ESTADO",null=True, blank=True)
    porc_sobregiro_credito = models.IntegerField(verbose_name= "PORC_SOBREGIRO_CREDITO")
    autorizacion_egresos_caja = models.CharField(verbose_name="AUTORIZACION_EGRESOS_CAJA")
    apertura_caja_requerido = models.CharField(verbose_name= "APERTURA_CAJA_REQUERIDO")
    cod_usuario = models.ForeignKey(ADUsuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'AD_USUARIO_EMPRESA'
        constraints = [
            models.UniqueConstraint(fields=['COD_EMPRESA', 'cod_usuario'], name='AD_USUARIO_X_EMPRESAL_PK')
        ]


class adUsuarioAgencia(models.Model):
   cod_empresa = models.CharField(max_length=8 ,  verbose_name="COD_EMPRESA")
   cod_agencia = models.CharField(max_length=8,  verbose_name="COD_AGENCIA")
   cod_usuario = models.ForeignKey(ADUsuario, on_delete=models.CASCADE)
   estado = models.IntegerField(verbose_name="ESTADO", null=True, blank=True)

   class Meta:
        db_table = 'AD_USUARIO_AGENCIA'
        constraints = [
            models.UniqueConstraint(fields=['cod_empresa','cod_agencia', 'cod_usuario'], name='AD_USUARIO_X_AGENCIA_PK')
        ]
        unique_together = (('cod_agencia', 'cod_empresa'),('cod_empresa', 'cod_usuario'))



