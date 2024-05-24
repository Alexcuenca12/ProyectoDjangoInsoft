# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class AdUsuario(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     cod_usuario = models.CharField(primary_key=True, max_length=30)
#     nombre = models.CharField(max_length=60)
#     pw_app = models.CharField(max_length=30, blank=True, null=True)
#     pw_bd = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'AD_USUARIO'
#
#
# class AdUsuarioAgencia(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cod_empresa = models.CharField(max_length=8)
#     cod_agencia = models.CharField(max_length=8)
#     estado = models.IntegerField(blank=True, null=True)
#     cod_usuario = models.ForeignKey(AdUsuario, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'AD_USUARIO_AGENCIA'
#         unique_together = (('cod_empresa', 'cod_agencia', 'cod_usuario'), ('cod_agencia', 'cod_empresa'), ('cod_empresa', 'cod_usuario'),)
#
#
# class AdUsuarioEmpresa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     cod_empresa = models.CharField(db_column='COD_EMPRESA', max_length=8)  # Field name made lowercase.
#     estado = models.IntegerField(blank=True, null=True)
#     porc_sobregiro_credito = models.IntegerField()
#     autorizacion_egresos_caja = models.CharField()
#     apertura_caja_requerido = models.CharField()
#     cod_usuario = models.ForeignKey(AdUsuario, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'AD_USUARIO_EMPRESA'
#         unique_together = (('cod_empresa', 'cod_usuario'),)
#
#
# class AdUsuarioGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     adusuario = models.ForeignKey(AdUsuario, models.DO_NOTHING)
#     group = models.ForeignKey('AuthGroup', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'AD_USUARIO_groups'
#         unique_together = (('adusuario', 'group'),)
#
#
# class AdUsuarioUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     adusuario = models.ForeignKey(AdUsuario, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'AD_USUARIO_user_permissions'
#         unique_together = (('adusuario', 'permission'),)
#
#
# class AdAgencia(models.Model):
#     cod_empresa = models.CharField(max_length=8)
#     cod_agencia = models.CharField(primary_key=True, max_length=8, db_comment='Campo que identifica el registro (el secuencial forma parte de la clave primaria)')  # The composite primary key (cod_agencia, cod_empresa) found, that is not supported. The first column is selected.
#     nombre = models.CharField(max_length=60, db_comment='Campo que define el nombre de las agencias registradas en el sistema')
#     estado = models.IntegerField(db_comment='Campo que identifica si la agencia se encuentra disponible o no.')
#     cod_producto = models.CharField(max_length=8, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ad_agencia'
#         unique_together = (('cod_agencia', 'cod_empresa'),)
#         db_table_comment = 'La tabla AD_Agencia permite registrar todas las agencias asociadas a una determinada empresa que estarßn disponibles en el sistema'
#
#
#
#
#
#
#
#
#
# class AdFormulas(models.Model):
#     cod_empresa = models.CharField(max_length=8)
#     cod_tipo_formula = models.ForeignKey('EnCatalogo', models.DO_NOTHING, db_column='cod_tipo_formula')
#     cod_formula = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_formula, cod_empresa, cod_tipo_formula) found, that is not supported. The first column is selected.
#     nombre = models.CharField(max_length=100)
#     observaciones = models.CharField(max_length=500, blank=True, null=True)
#     definicion = models.CharField(max_length=2000)
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
#     audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro. ')
#     audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
#
#     class Meta:
#         managed = False
#         db_table = 'ad_formulas'
#         unique_together = (('cod_formula', 'cod_empresa', 'cod_tipo_formula'),)
#
#
# class AdFrecuenciasTiempo(models.Model):
#     cod_empresa = models.CharField(max_length=8)
#     cod_frecuencia = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_frecuencia, cod_empresa) found, that is not supported. The first column is selected.
#     nombre = models.CharField(max_length=100)
#     valor_frecuencia = models.DecimalField(max_digits=10, decimal_places=0)
#     tipo_frecuencia = models.CharField(max_length=3)
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la relacion')
#     audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la relacion en el sistema')
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien realizo la ultima actualizacion de la relacion')
#     audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la relacion en el sistema')
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ad_frecuencias_tiempo'
#         unique_together = (('cod_frecuencia', 'cod_empresa'),)
#
#
# class AdFuncionCab(models.Model):
#     cod_funcion = models.CharField(primary_key=True, max_length=8)
#     nombre = models.CharField(max_length=60)
#     nombre_bd = models.CharField(max_length=100)
#     return_field = models.CharField(db_column='return', max_length=3)  # Field renamed because it was a Python reserved word.
#     observaciones = models.CharField(max_length=200, blank=True, null=True)
#     cod_tipo_funcion = models.ForeignKey('EnCatalogo', models.DO_NOTHING, db_column='cod_tipo_funcion')
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
#     audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro.')
#     audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
#     campo = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ad_funcion_cab'
#
#
# class AdFuncionDet(models.Model):
#     cod_funcion = models.ForeignKey(AdFuncionCab, models.DO_NOTHING, db_column='cod_funcion')
#     secuencia = models.DecimalField(primary_key=True, max_digits=3, decimal_places=0)  # The composite primary key (secuencia, cod_funcion) found, that is not supported. The first column is selected.
#     tipo_parametro = models.CharField(max_length=3)
#     cod_parametro = models.CharField(max_length=12, blank=True, null=True)
#     parametro_char = models.CharField(max_length=20, blank=True, null=True)
#     parametro_number = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
#     audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro.')
#     audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
#
#     class Meta:
#         managed = False
#         db_table = 'ad_funcion_det'
#         unique_together = (('secuencia', 'cod_funcion'),)
#
#
# class AdParametros(models.Model):
#     cod_empresa = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_empresa, cod_parametro) found, that is not supported. The first column is selected.
#     cod_parametro = models.CharField(max_length=15)
#     nombre = models.CharField(max_length=100)
#     valor = models.CharField(max_length=100, blank=True, null=True)
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
#     audit_fecha_ing = models.DateField(blank=True, null=True)
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
#     audit_fecha_mod = models.DateField(blank=True, null=True)
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
#     observaciones = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ad_parametros'
#         unique_together = (('cod_empresa', 'cod_parametro'),)
#
#
#
# #
# #
# # class AdTipoEstadoXTipoTrx(models.Model):
# #     cod_empresa = models.OneToOneField(AdTipoEstado, models.DO_NOTHING, db_column='cod_empresa', primary_key=True)  # The composite primary key (cod_empresa, cod_tipo_transaccion) found, that is not supported. The first column is selected.
# #     cod_tipo_transaccion = models.ForeignKey('AdTipoTrx', models.DO_NOTHING, db_column='cod_tipo_transaccion')
# #     cod_tipo_estado = models.CharField(max_length=8)
# #
# #     class Meta:
# #         managed = False
# #         db_table = 'ad_tipo_estado_x_tipo_trx'
# #         unique_together = (('cod_empresa', 'cod_tipo_transaccion'),)
#
#
# class AdTipoTrx(models.Model):
#     cod_tipo_transaccion = models.CharField(primary_key=True, max_length=8)
#     nombre = models.CharField(max_length=80)
#     tipo = models.CharField(max_length=3, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ad_tipo_trx'
#
#
# class AdVariables(models.Model):
#     cod_empresa = models.CharField(max_length=8)
#     cod_tipo_variables = models.ForeignKey('EnCatalogo', models.DO_NOTHING, db_column='cod_tipo_variables')
#     cod_variable = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_variable, cod_tipo_variables, cod_empresa) found, that is not supported. The first column is selected.
#     nombre = models.CharField(max_length=100)
#     observaciones = models.CharField(max_length=500, blank=True, null=True)
#     estado = models.SmallIntegerField()
#     cod_funcion = models.ForeignKey(AdFuncionCab, models.DO_NOTHING, db_column='cod_funcion')
#     audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que creo el registro.')
#     audit_fecha_ing = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue creado el registro en el sistema')
#     audit_ip_ing = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde fue creado el registro')
#     audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el Usuario que realizo la ultima modificacion del registro.')
#     audit_fecha_mod = models.DateField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion del registro.')
#     audit_ip_mod = models.CharField(max_length=20, blank=True, null=True, db_comment='Campo que indica la IP donde se realizo la ultima actualizacion')
#
#     class Meta:
#         managed = False
#         db_table = 'ad_variables'
#         unique_together = (('cod_variable', 'cod_tipo_variables', 'cod_empresa'),)
#
#
#
#





























































class EnTipoDigital(models.Model):
    cod_tipo_digital = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    extension = models.CharField(max_length=200)
    estado = models.SmallIntegerField()
    cod_tipo_archivo = models.ForeignKey(EnCatalogo, models.DO_NOTHING, db_column='cod_tipo_archivo')
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien creo la relacion')
    audit_fecha_ing = models.DateTimeField(blank=True, null=True, db_comment='Campo que indica cuando fue creada la relacion en el sistema')
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True, db_comment='Campo que indica el usuario de aplicacion quien realizo la ultima actualizacion de la relacion')
    audit_fecha_mod = models.DateTimeField(blank=True, null=True, db_comment='Campo que indica cuando fue realizada la ultima actualizacion a los datos de la relacion en el sistema')
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_tipo_digital'



