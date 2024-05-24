from django.db import models

# Create your models here.
class AdFuncionCab(models.Model):
    cod_funcion = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=60)
    nombre_bd = models.CharField(max_length=100)
    return_field = models.CharField(db_column='return', max_length=3)  # Field renamed because it was a Python reserved word.
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    cod_tipo_funcion = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_tipo_funcion')
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro.')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
    campo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_funcion_cab'


class AdFuncionDet(models.Model):
    cod_funcion = models.ForeignKey(AdFuncionCab, models.DO_NOTHING, db_column='cod_funcion')
    secuencia = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)  # The composite primary key (secuencia, cod_funcion) found, that is not supported. The first column is selected.
    tipo_parametro = models.CharField(max_length=3)
    cod_parametro = models.CharField(max_length=12, blank=True, null=True)
    parametro_char = models.CharField(max_length=20, blank=True, null=True)
    parametro_number = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro.')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')

    class Meta:
        managed = False
        db_table = 'ad_funcion_det'
        unique_together = (('secuencia', 'cod_funcion'),)