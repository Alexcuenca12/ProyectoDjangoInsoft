from django.db import models

from catalogo.models import EnCatalogo


# Create your models here.
class AdTipoEstado(models.Model):
    cod_empresa = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_empresa, cod_tipo_estado) found, that is not supported. The first column is selected.
    cod_tipo_estado = models.CharField(max_length=8)
    nombre = models.CharField(max_length=80)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la opci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la opci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la opci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realiz¾ la ·ltima actualizaci¾n')

    class Meta:
        managed = False
        db_table = 'ad_tipo_estado'
        unique_together = (('cod_empresa', 'cod_tipo_estado'),)

class AdTipoEstadoXTipoTrx(models.Model):
    cod_empresa = models.OneToOneField(AdTipoEstado, models.DO_NOTHING, db_column='cod_empresa', primary_key=True)  # The composite primary key (cod_empresa, cod_tipo_transaccion) found, that is not supported. The first column is selected.
    cod_tipo_transaccion = models.ForeignKey('AdTipoTrx', models.DO_NOTHING, db_column='cod_tipo_transaccion')
    cod_tipo_estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ad_tipo_estado_x_tipo_trx'
        unique_together = (('cod_empresa', 'cod_tipo_transaccion'),)


class AdTipoTrx(models.Model):
    cod_tipo_transaccion = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=80)
    tipo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_tipo_trx'


class EnTipoDigital(models.Model):
    cod_tipo_digital = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    extension = models.CharField(max_length=200)
    estado = models.SmallIntegerField()
    cod_tipo_archivo = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_tipo_archivo')
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la relacion')
    audit_fecha_ing = models.DateTimeField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la relacion en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien realizo la ultima actualizacion de la relacion')
    audit_fecha_mod = models.DateTimeField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la relacion en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_tipo_digital'