from django.db import models

from empresa.models import AdEmpresa


#
# from BaseModelo.models import BaseModel
# from empresa.models import AdEmpresa
#
#
class EnTipoCatalogo(models.Model):
    cod_tipo_catalogo = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=60)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_ing = models.DateField(blank=True, null=True)
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True)
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_tipo_catalogo'
class EnCatalogo(models.Model):
    cod_catalogo = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=60)
    cod_tipo_catalogo = models.ForeignKey('EnTipoCatalogo', models.DO_NOTHING, db_column='cod_tipo_catalogo')
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_ing = models.DateField(blank=True, null=True)
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True)
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_catalogo'

class EnCatalogoXEmpresa(models.Model):
    cod_empresa = models.ForeignKey('empresa.AdEmpresa', models.DO_NOTHING, db_column='cod_empresa')
    cod_catalogo = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_catalogo, cod_empresa) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=100)
    cod_tipo_catalogo = models.ForeignKey('EnTipoCatalogo', models.DO_NOTHING, db_column='cod_tipo_catalogo')

    class Meta:
        managed = False
        db_table = 'en_catalogo_x_empresa'
        unique_together = (('cod_catalogo', 'cod_empresa'),)
