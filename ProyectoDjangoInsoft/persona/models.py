from django.db import models

from BaseModelo.models import BaseModel


# from geo.models import EnGeo
# from tipo.models import EnTipoDigital


#
# # Create your models here.
#
class EnPersona(models.Model):
    cod_persona = models.BigIntegerField(primary_key=True)
    tipo_persona = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='tipo_persona')
    primer_nombre = models.CharField(max_length=25, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=25, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=25, blank=True, null=True)
    apellido_materno = models.CharField(max_length=25, blank=True, null=True)
    nombres = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado_civil = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='estado_civil', related_name='enpersona_estado_civil_set', blank=True, null=True)
    genero = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='genero', related_name='enpersona_genero_set', blank=True, null=True)
    cod_pais_nace = models.CharField(max_length=8, blank=True, null=True)
    cod_lugar_nace = models.CharField(max_length=8, blank=True, null=True)
    cod_pais_nacionalidad = models.CharField(max_length=8, blank=True, null=True)
    cod_ocupacion = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_ocupacion', related_name='enpersona_cod_ocupacion_set', blank=True, null=True)
    cod_profesion = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_profesion', related_name='enpersona_cod_profesion_set', blank=True, null=True)
    estado = models.SmallIntegerField()
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    separacion_bienes = models.CharField(max_length=1, blank=True, null=True)
    tipo_vivienda = models.CharField(max_length=3, blank=True, null=True)
    num_cargas = models.SmallIntegerField(blank=True, null=True)
    nro_hijos = models.SmallIntegerField(blank=True, null=True)
    nombre_comercial = models.CharField(max_length=100, blank=True, null=True)
    cod_conyuge = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_conyuge', blank=True, null=True)
    nombre_arrendatario_vivienda = models.CharField(max_length=80, blank=True, null=True)
    telefono_arrendatario_vivienda = models.CharField(max_length=20, blank=True, null=True)
    tipo_local = models.CharField(max_length=3, blank=True, null=True)
    nombre_arrendatario_local = models.CharField(max_length=80, blank=True, null=True)
    telefono_arrendatario_local = models.CharField(max_length=80, blank=True, null=True)
    fecha_establecido_negocio = models.DateField(blank=True, null=True)
    fecha_inicio_actividad_econ = models.DateField(blank=True, null=True)
    codigo_referencia = models.CharField(max_length=20, blank=True, null=True)
    clase_contribuyente = models.CharField(max_length=10, blank=True, null=True)
    obligado_contribuyente = models.CharField(max_length=2, blank=True, null=True)
    actividad_economica = models.CharField(max_length=2000, blank=True, null=True)
    cod_empresa_caja_chica = models.CharField(max_length=8, blank=True, null=True)
    tipo_persona_sri = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_persona'
#
#
#
class EnDireccionesXPersona(models.Model):
    cod_persona = models.ForeignKey('EnPersona', models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    cod_direccion = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_direccion')
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=10, blank=True, null=True)
    interseccion = models.CharField(max_length=80, blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)
    barrio = models.CharField(max_length=80, blank=True, null=True)
    cod_pais = models.CharField(max_length=8)
    cod_lugar = models.ForeignKey('geo.EnGeo', models.DO_NOTHING, db_column='cod_lugar')
    principal = models.CharField(max_length=1, blank=True, null=True)
    coordenada_x = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    coordenada_y = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_direcciones_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)

class EnElectronicosXPersona(models.Model):
    cod_persona = models.OneToOneField('persona.EnPersona', models.DO_NOTHING, db_column='cod_persona', primary_key=True)  # The composite primary key (cod_persona, secuencia) found, that is not supported. The first column is selected.
    secuencia = models.IntegerField()
    cod_catalogo = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_catalogo')
    contacto = models.CharField(max_length=800)
    principal = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_electronicos_x_persona'
        unique_together = (('cod_persona', 'secuencia'),)
class EnTelefonosXPersona(models.Model):
    cod_persona = models.ForeignKey(EnPersona, models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    cod_telefono = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_telefono')
    telefono = models.CharField(max_length=100)
    principal = models.CharField(max_length=1, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_telefonos_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)
class EnIdentificacionesXPersona(models.Model):
    cod_persona = models.OneToOneField('persona.EnPersona', models.DO_NOTHING, db_column='cod_persona', primary_key=True)  # The composite primary key (cod_persona, cod_identificacion) found, that is not supported. The first column is selected.
    cod_identificacion = models.ForeignKey('catalogo.EnCatalogo', models.DO_NOTHING, db_column='cod_identificacion')
    identificacion = models.CharField(max_length=20)
    principal = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'en_identificaciones_x_persona'
        unique_together = (('cod_persona', 'cod_identificacion'), ('identificacion', 'cod_identificacion'),)
class EnDigitalesXPersona(models.Model):
    cod_persona = models.ForeignKey('EnPersona', models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    cod_tipo_digital = models.ForeignKey('tipo.EnTipoDigital', models.DO_NOTHING, db_column='cod_tipo_digital')
    archivo = models.BinaryField(blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien cre¾ la relaci¾n')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue creada la relaci¾n en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicaci¾n quien realiz¾ la ·ltima actualizaci¾n de la relaci¾n')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cußndo fue realizada la ·ltima actualizaci¾n a los datos de la relaci¾n en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    extension = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_digitales_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)
class EnBienesXPersona(models.Model):
    cod_persona = models.ForeignKey('persona.EnPersona', models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    tipo_bien = models.CharField(max_length=3)
    avaluo = models.DecimalField(max_digits=22, decimal_places=8)
    hipotecado = models.CharField(max_length=1)
    institucion_hipoteca = models.CharField(max_length=50, blank=True, null=True)
    secuencia_digital = models.ForeignKey('EnDigitalesXPersona', models.DO_NOTHING, db_column='secuencia_digital', blank=True, null=True)
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
        db_table = 'en_bienes_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)

class EnVehiculosXPersona(models.Model):
    cod_persona = models.ForeignKey('persona.EnPersona', models.DO_NOTHING, db_column='cod_persona')
    secuencia = models.IntegerField(primary_key=True)  # The composite primary key (secuencia, cod_persona) found, that is not supported. The first column is selected.
    marca = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    anio = models.IntegerField()
    avaluo = models.DecimalField(max_digits=22, decimal_places=8)
    prendado = models.CharField(max_length=1)
    institucion_prendado = models.CharField(max_length=50, blank=True, null=True)
    secuencia_digital = models.ForeignKey(EnDigitalesXPersona, models.DO_NOTHING, db_column='secuencia_digital', blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro. ')
    audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro. ')
    audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
    direccion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=150, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_vehiculos_x_persona'
        unique_together = (('secuencia', 'cod_persona'),)
