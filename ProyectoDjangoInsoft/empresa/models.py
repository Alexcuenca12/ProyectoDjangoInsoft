from django.db import models

# Create your models here.
class ADEmpresa():
    cod_empresa = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    estado = models.IntegerField()
    cod_persona = models.IntegerField()
   # logo = models.
    nro_establecimientos_activos = models.IntegerField()
    nro_resolucion_contrib_esp = models.IntegerField()
    fecha_nro_resolucion =models.DateField()
    nombre_archivo_firma = models.CharField(max_length=60)
    clave_firma = models.CharField(max_length=256)
    fecha_caduca_firma = models.DateField()
   # cod_rol = models.CharField(max_length=)
    crm = models.CharField(max_length=1)

    class Meta:
        db_table = 'ADE_EMPRESAS'
        constraints = [
            models.UniqueConstraint(fields=['cod_empresa'], name='AD_EMPRESA_PK'),
            models.ForeignKeyConstraint(fields=['cod_persona'], to='P_persona.en_persona',
                                        name='AD_EMPRESA_EN_PERSONA_FK'),
            #models.ForeignKeyConstraint(fields=['cod_rol'], to='nombreapp.ad_rol', name='AD_EMP_ROL_FK')
        ]
