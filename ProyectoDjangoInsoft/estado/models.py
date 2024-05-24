from django.db import models

from BaseModelo.models import BaseModel

class AdEstado(models.Model):
    cod_empresa = models.ForeignKey('tipo.AdTipoEstado', models.DO_NOTHING, db_column='cod_empresa')
    cod_tipo_estado = models.CharField(max_length=8)
    cod_estado = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_estado, cod_tipo_estado, cod_empresa) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=80)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la opci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la opci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la opci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realiz¾ la ·ltima actualizaci¾n')
    estado_inicial = models.CharField(max_length=1)
    activo_inactivo = models.CharField(max_length=1)
    permite_procesos = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ad_estado'
        unique_together = (('cod_estado', 'cod_tipo_estado', 'cod_empresa'),)
#
class AdEstadoTransicion(models.Model):
    cod_empresa = models.OneToOneField('tipo.AdTipoEstado', models.DO_NOTHING, db_column='cod_empresa', primary_key=True)  # The composite primary key (cod_empresa, cod_tipo_estado, cod_estado_desde, cod_estado_hasta) found, that is not supported. The first column is selected.
    cod_tipo_estado = models.CharField(max_length=8)
    cod_estado_desde = models.ForeignKey(AdEstado, models.DO_NOTHING, db_column='cod_estado_desde')
    cod_estado_hasta = models.ForeignKey(AdEstado, models.DO_NOTHING, db_column='cod_estado_hasta', related_name='adestadotransicion_cod_estado_hasta_set')
    estado = models.IntegerField()
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la opcion')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la opcion en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la opcion en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
    afecta_cabecera_detalle = models.CharField(max_length=2)
    cod_tipo_inventario = models.CharField(max_length=8)
    signo = models.CharField(max_length=1, blank=True, null=True)
    transicion_automatica = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_estado_transicion'
        unique_together = (('cod_empresa', 'cod_tipo_estado', 'cod_estado_desde', 'cod_estado_hasta'),)

#
