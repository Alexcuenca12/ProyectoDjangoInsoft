from django.db import models

from catalogo.models import EnCatalogo
from persona.models import EnPersona


#
# from BaseModelo.models import BaseModel
# from catalogo.models import EnCatalogo
#
#
#
# # Create your models here.
#
class EnReferenciasCab(models.Model):
    cod_persona = models.OneToOneField(EnPersona, models.DO_NOTHING, db_column='cod_persona', primary_key=True)  # The composite primary key (cod_persona, secuencia) found, that is not supported. The first column is selected.
    secuencia = models.IntegerField()
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    cod_tipo_referencia = models.ForeignKey(EnCatalogo, models.DO_NOTHING, db_column='cod_tipo_referencia')
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la relaci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la relaci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien realiz¾ la ·ltima actualizaci¾n de la relaci¾n')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la relaci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_referencias_cab'
        unique_together = (('cod_persona', 'secuencia'),)

class EnRefBancariasXPersona(models.Model):
    cod_persona = models.ForeignKey(EnPersona, models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.BigIntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    cod_entidad = models.CharField(max_length=8)
    tipo_cuenta = models.ForeignKey(EnCatalogo, models.DO_NOTHING, db_column='tipo_cuenta')
    nro_cuenta = models.CharField(max_length=30)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la relacion')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la relacion en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien realizo la ultima actualizacion de la relacion')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la relacion en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    obtenido_credito = models.CharField(max_length=1, blank=True, null=True)
    monto_credito = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    fecha_apertura_cuenta = models.DateField(blank=True, null=True)
    cupo = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_ref_bancarias_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)
class EnRefComercialesXPersona(models.Model):
    cod_persona = models.ForeignKey(EnPersona, models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    nombre_comercio = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=22, decimal_places=8)
    fecha_ult_compra = models.DateField(blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la relaci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la relaci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien realiz¾ la ·ltima actualizaci¾n de la relaci¾n')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la relaci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    telefono_comercio = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_ref_comerciales_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)


class EnRefLaboralesXPersona(models.Model):
    cod_persona = models.ForeignKey(EnPersona, models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.BigIntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    empresa_labora = models.CharField(max_length=60)
    sueldo = models.DecimalField(max_digits=22, decimal_places=8)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la relacion')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la relacion en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien realizo la ultima actualizacion de la relacion')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la relacion en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_ref_laborales_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)

class EnRefPersonalesXPersona(models.Model):
    cod_persona = models.IntegerField()
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    nombre_ref_personal = models.CharField(max_length=100)
    parentesco = models.ForeignKey(EnCatalogo, models.DO_NOTHING, db_column='parentesco')
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la relaci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la relaci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien realiz¾ la ·ltima actualizaci¾n de la relaci¾n')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la relaci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_ref_personales_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)
#
#

