from django.db import models

from BaseModelo.models import BaseModel


#from BaseModelo.models import BaseModel


# Create your models here.

class en_catalogo(BaseModel):
    objects = None
    COD_CATALOGO= models.IntegerField(primary_key=True, unique=True, verbose_name="COD_CATALOGO")
    #COD_CATALOGO= models.BigAutoField(primary_key=True)
    NOMBRE = models.CharField(max_length=60, verbose_name="NOMBRE")


    # es to string
    def __str__(self):
        return self.NOMBRE

    class Meta:
        db_table = 'EN_CATALOGO'

    # para referenciar instancias de este modelo en las  relaciones.
    def natural_key(self):
        return (self.COD_CATALOGO)

class en_persona (models.Model):

    COD_PERSONA = models.IntegerField(primary_key=True, unique=True, verbose_name="EN_PERSONA_PK")
    # COD_PERSONA = models.BigAutoField(primary_key=True)
    PRIMER_NOMBRE = models.CharField(max_length=25, verbose_name="PRIMER_NOMBRE")
    SEGUNDO_NOMBRE = models.CharField(max_length=25,  verbose_name="SEGUNDO_NOMBRE")
    APELLIDO_PATERNO = models.CharField(max_length=25, verbose_name="APELLIDO_PATERNO")
    APELLIDO_MATERNO = models.CharField(max_length=25, verbose_name="APELLIDO_MATERNO")
    NOMBRES = models.CharField(max_length=200, verbose_name="NOMBRES")
    FECHA_NACIMIENTO = models.DateField(verbose_name="FECHA_NACIMIENTO")
    ESTADO = models.IntegerField( verbose_name="ESTADO")
    OBSERVACIONES = models.CharField(max_length=200, verbose_name="OBSERVACIONES",null=True, blank=True)
    SEPARACION_BIENES = models.CharField(max_length=1,verbose_name="SEPARACION_BIENES",null=True, blank=True)
    TIPO_VIVIENDA = models.CharField(max_length=3,verbose_name="TIPO_VIVIENDA",null=True, blank=True)
    NUM_CARGAS = models.IntegerField(verbose_name="NUM_CARGAS",null=True, blank=True)
    NRO_HIJOS = models.IntegerField(verbose_name="NRO_HIJOS",null=True, blank=True)
    NOMBRE_COMERCIAL = models.CharField(max_length=100,verbose_name="NOMBRE_COMERCIAL",null=True, blank=True)
    NOMBRE_ARRENDATARIO_VIVIENDA = models.CharField(max_length=80,verbose_name="NOMBRE_ARRENDATARIO_VIVIENDA",null=True, blank=True)
    TELEFONO_ARRENDATARIO_VIVIENDA = models.CharField(max_length=20 ,verbose_name="TELEFONO_ARRENDATARIO_VIVIENDA",null=True, blank=True)
    TIPO_LOCAL = models.CharField(max_length=3, verbose_name="TIPO_LOCAL",null=True, blank=True)
    NOMBRE_ARRENDATARIO_LOCAL = models.CharField(max_length=80,verbose_name="NOMBRE_ARRENDATARIO_LOCAL",null=True, blank=True)
    TELEFONO_ARRENDATARIO_LOCAL = models.CharField(max_length=80 , verbose_name="TELEFONO_ARRENDATARIO_LOCAL",null=True, blank=True)
    FECHA_ESTABLECIDO_NEGOCIO = models.DateField(verbose_name="FECHA_ESTABLECIDO_NEGOCIO",null=True, blank=True)
    FECHA_INICIO_ACTIVIDAD_ECON = models.DateField(verbose_name="FECHA_INICIO_ACTIVIDAD_ECON",null=True, blank=True)
    CODIGO_REFERENCIA = models.CharField(max_length=20, verbose_name="CODIGO_REFERENCIA",null=True, blank=True)
    CLASE_CONTRIBUYENTE = models.CharField(max_length=10, verbose_name="CLASE_CONTRIBUYENTE",null=True, blank=True)
    OBLIGADO_CONTRIBUYENTE = models.CharField(max_length=2, verbose_name="OBLIGADO_CONTRIBUYENTE",null=True, blank=True)
    ACTIVIDAD_ECONOMICA = models.CharField(max_length=2000, verbose_name="ACTIVIDAD_ECONOMICA",null=True, blank=True)
    TIPO_PERSONA_SRI = models.CharField(max_length=8, verbose_name="TIPO_PERSONA_SRI",null=True, blank=True)



    #  llaves fk

    # Relación con EnPersona (Cod_Conyuge)
    cod_conyuge = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='EN_PERSONA_CONYUGE_FK',
                                    verbose_name="COD_CONYUGE")
    COD_OCUPACION = models.ForeignKey(en_catalogo, on_delete=models.CASCADE, related_name='EN_PERSONA_EN_CATALOGO_FK',
                                      verbose_name="COD_OCUPACION", null=True)
    COD_PROFESION = models.ForeignKey(en_catalogo, on_delete=models.CASCADE, related_name='EN_PERSONA_EN_CATALOGO_FKV1',
                                      verbose_name="COD_PROFESION",null=True)
    TIPO_PERSONA = models.ForeignKey(en_catalogo, on_delete=models.CASCADE, related_name='EN_PERSONA_EN_CATALOGO_FKV2',
                                      verbose_name="TIPO_PERSONA", null=True)
    ESTADO_CIVIL = models.ForeignKey(en_catalogo, on_delete=models.CASCADE, related_name='EN_PERSONA_EN_CATALOGO_FKV3',
                                      verbose_name="ESTADO_CIVIL", null=True)
    GENERO = models.ForeignKey(en_catalogo, on_delete=models.CASCADE, related_name='EN_PERSONA_EN_CATALOGO_FKV4',
                                      verbose_name="GENERO", null=True)

    #es to string
    def __str__(self):
        return self.NOMBRES

    class Meta:
        db_table ='EN_PERSONA' # nombre del atabla en bd

    # para referenciar instancias de este modelo en las  relaciones.
    def natural_key(self):
        return (self.COD_PERSONA)




class EnDireccion(models.Model):
    cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE)
    secuencia = models.IntegerField()
    cod_direccion = models.ForeignKey(en_catalogo, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=10, blank=True, null=True)
    interseccion = models.CharField(max_length=80, blank=True, null=True)
    referencia = models.CharField(max_length=200, blank=True, null=True)
    barrio = models.CharField(max_length=80, blank=True, null=True)
    cod_pais = models.CharField(max_length=8)
    cod_lugar = models.CharField(max_length=8)
    principal = models.CharField(max_length=1, blank=True, null=True)
    coordenada_x = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)
    coordenada_y = models.DecimalField(max_digits=22, decimal_places=8, blank=True, null=True)

    class Meta:
        db_table = 'EN_DIRECCIONES_X_PERSONA'
        unique_together = (('secuencia', 'cod_persona'),)

class EnElectronicos(models.Model):
    cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE)
    secuencia = models.IntegerField()
    cod_catalogo = models.ForeignKey(en_catalogo, on_delete=models.CASCADE)
    contacto = models.CharField(max_length=800)
    principal = models.CharField(max_length=1)

    class Meta:
        db_table = 'EN_ELECTRONICOS_X_PERSONA'
        constraints = [
            models.UniqueConstraint(fields=['cod_persona', 'secuencia'], name='EN_ELECTRONICOS_X_PERSONA_PK')
        ]

class EnTelefonos(models.Model):
    cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE)
    secuencia = models.IntegerField()
    cod_telefono = models.ForeignKey(en_catalogo, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=100)
    principal = models.CharField(max_length=1)
    extension = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'EN_TELEFONOS_X_PERSONA'
        constraints = [
            models.UniqueConstraint(fields=['secuencia', 'cod_persona'], name='EN_TELEFONOS_X_PERSONA_PK')
        ]

class EnIdentificaciones(models.Model):
    cod_persona = models.ForeignKey(en_persona, on_delete=models.CASCADE)
    cod_identificacion = models.ForeignKey(en_catalogo, on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=20)
    principal = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = 'EN_IDENTIFICACIONES_X_PERSONA'
        constraints = [
            models.UniqueConstraint(fields=['cod_persona', 'cod_identificacion'], name='EN_IDENTIFICA_X_PERSONA_PK')
        ]
