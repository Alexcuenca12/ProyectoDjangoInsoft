from django.db import models




class AdEmpresa(models.Model):
    cod_empresa = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=60)
    estado = models.IntegerField()
    cod_persona = models.ForeignKey('persona.EnPersona', models.DO_NOTHING, db_column='cod_persona', blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    nro_establecimientos_activos = models.IntegerField(blank=True, null=True)
    nro_resolucion_contrib_esp = models.IntegerField(blank=True, null=True)
    fecha_nro_resolucion = models.DateField(blank=True, null=True)
    nombre_archivo_firma = models.CharField(max_length=60, blank=True, null=True)
    clave_firma = models.CharField(max_length=256, blank=True, null=True)
    fecha_caduca_firma = models.DateField(blank=True, null=True)
    cod_rol = models.CharField(max_length=8, blank=True, null=True)
    crm = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ad_empresa'