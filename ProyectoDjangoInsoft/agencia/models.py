from django.db import models

# Create your models here.
class AdAgencia(models.Model):
    cod_empresa = models.CharField(max_length=8)
    cod_agencia = models.CharField(primary_key=True, max_length=8, db_comment='Campo que identifica el registro (el secuencial forma parte de la clave primaria)')  # The composite primary key (cod_agencia, cod_empresa) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=60, db_comment='Campo que define el nombre de las agencias registradas en el sistema')
    estado = models.IntegerField(db_comment='Campo que identifica si la agencia se encuentra disponible o no.')
    cod_producto = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_agencia'
        unique_together = (('cod_agencia', 'cod_empresa'),)
        db_table_comment = 'La tabla AD_Agencia permite registrar todas las agencias asociadas a una determinada empresa que estarßn disponibles en el sistema'

