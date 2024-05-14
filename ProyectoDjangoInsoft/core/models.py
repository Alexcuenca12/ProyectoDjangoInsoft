from django.db import models

# Create your models here.

class en_catalogo(models.Model):


    COD_CATALOGO= models.IntegerField(primary_key=True, unique=True, verbose_name="COD_CATALOGO")
    NOMBRE = models.CharField(max_length=60, verbose_name="NOMBRE")
    AUDIT_USUARIO_ING = models.CharField(max_length=30,verbose_name="AUDIT_USUARIO_ING")
    AUDIT_FECHA_ING = models.DateField(verbose_name="AUDIT_FECHA_ING")
    AUDIT_IP_ING = models.CharField(max_length=20, verbose_name="AUDIT_IP_ING")
    AUDIT_USUARIO_MOD = models.CharField(max_length=30, verbose_name="AUDIT_USUARIO_MOD")
    AUDIT_FECHA_MOD = models.DateField(verbose_name="AUDIT_FECHA_MOD")
    AUDIT_IP_MOD = models.CharField(max_length=20, verbose_name="AUDIT_IP_MOD")

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
    PRIMER_NOMBRE = models.CharField(max_length=25, verbose_name="PRIMER_NOMBRE")
    SEGUNDO_NOMBRE = models.CharField(max_length=25,  verbose_name="SEGUNDO_NOMBRE")
    APELLIDO_PATERNO = models.CharField(max_length=25, verbose_name="APELLIDO_PATERNO")
    APELLIDO_MATERNO = models.CharField(max_length=25, verbose_name="APELLIDO_MATERNO")
    NOMBRES = models.CharField(max_length=200, verbose_name="NOMBRES")
    FECHA_NACIMIENTO = models.DateField(verbose_name="FECHA_NACIMIENTO")
    ESTADO = models.IntegerField( verbose_name="ESTADO")
    OBSERVACIONES = models.CharField(max_length=200, verbose_name="OBSERVACIONES")
    SEPARACION_BIENES = models.CharField(max_length=1,verbose_name="SEPARACION_BIENES")
    TIPO_VIVIENDA = models.CharField(max_length=3,verbose_name="TIPO_VIVIENDA")
    NUM_CARGAS = models.IntegerField(verbose_name="NUM_CARGAS")
    NRO_HIJOS = models.IntegerField(verbose_name="NRO_HIJOS")
    NOMBRE_COMERCIAL = models.CharField(max_length=100,verbose_name="NOMBRE_COMERCIAL")
    NOMBRE_ARRENDATARIO_VIVIENDA = models.CharField(max_length=80,verbose_name="NOMBRE_ARRENDATARIO_VIVIENDA")
    TELEFONO_ARRENDATARIO_VIVIENDA = models.CharField(max_length=20 ,verbose_name="TELEFONO_ARRENDATARIO_VIVIENDA")
    TIPO_LOCAL = models.CharField(max_length=3, verbose_name="TIPO_LOCAL")
    NOMBRE_ARRENDATARIO_LOCAL = models.CharField(max_length=80,verbose_name="NOMBRE_ARRENDATARIO_LOCAL")
    TELEFONO_ARRENDATARIO_LOCAL = models.CharField(max_length=80 , verbose_name="TELEFONO_ARRENDATARIO_LOCAL")
    FECHA_ESTABLECIDO_NEGOCIO = models.DateField(verbose_name="FECHA_ESTABLECIDO_NEGOCIO")
    FECHA_INICIO_ACTIVIDAD_ECON = models.DateField(verbose_name="FECHA_INICIO_ACTIVIDAD_ECON")
    CODIGO_REFERENCIA = models.CharField(max_length=20, verbose_name="CODIGO_REFERENCIA")
    CLASE_CONTRIBUYENTE = models.CharField(max_length=10, verbose_name="CLASE_CONTRIBUYENTE")
    OBLIGADO_CONTRIBUYENTE = models.CharField(max_length=2, verbose_name="OBLIGADO_CONTRIBUYENTE")
    ACTIVIDAD_ECONOMICA = models.CharField(max_length=2000, verbose_name="ACTIVIDAD_ECONOMICA")
    TIPO_PERSONA_SRI = models.CharField(max_length=8, verbose_name="TIPO_PERSONA_SRI")



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


