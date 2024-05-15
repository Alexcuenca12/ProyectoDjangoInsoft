from django.db import models
from django.forms import model_to_dict


# Create your models here.
class BaseModel(models.Model):


    AUDIT_USUARIO_ING = models.CharField(null=True,max_length=30, verbose_name="AUDIT_USUARIO_ING")
    AUDIT_FECHA_ING = models.DateField(null=True,verbose_name="AUDIT_FECHA_ING")
    AUDIT_IP_ING = models.CharField(null=True,max_length=20, verbose_name="AUDIT_IP_ING")
    AUDIT_USUARIO_MOD = models.CharField(null=True,max_length=30, verbose_name="AUDIT_USUARIO_MOD")
    AUDIT_FECHA_MOD = models.DateField(null=True,verbose_name="AUDIT_FECHA_MOD")
    AUDIT_IP_MOD = models.CharField(null=True,max_length=20, verbose_name="AUDIT_IP_MOD")

    class Meta:
        abstract = True

    # obtener el regostro(s) en formato JSON


