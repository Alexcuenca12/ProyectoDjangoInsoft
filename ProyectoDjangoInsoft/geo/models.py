from django.db import models

from BaseModelo.models import BaseModel


# Create your models here.
class EnGeo(BaseModel):
    cod_pais = models.CharField(max_length=8)
    cod_lugar = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    #llaves
    cod_org = models.IntegerField()
    cod_sri = models.CharField(max_length=8)
    cod_pais_padre = models.CharField(max_length=8)
    cod_icl = models.CharField()


    class Meta:
        db_table = 'EN_GEO'
        constraints = [
            models.UniqueConstraint(fields=['cod_lugar', 'cod_pais'], name='EN_GEO_PK')
            # LLAVES FORANEAS

        ]



class EnOrGeo(BaseModel):
    cod_pais = models.ForeignKey(EnGeo, on_delete=models.CASCADE)
    cod_org = models.IntegerField()
    nombre = models.CharField(max_length=60)

    class Meta:
        db_table = 'EN_ORG_GEO'
        constraints = [
            models.UniqueConstraint(fields=['cod_org', 'cod_pais'], name='EN_ORG_GEO_PK')
            # LLAVES FORANEAS

        ]



class EnPais(BaseModel):
    cod_pais = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    codigo_telefono = models.CharField(max_length=10)
    gentilicio = models.CharField(max_length=20)
    #llaves
    codigo_sri = models.CharField(max_length=20)
    convenio_doble_tributacion = models.CharField(max_length=2 , null=True, blank=True )
    certificado_origen = models.CharField(max_length=1)
    certificado_euro = models.CharField(max_length=1)

    class Meta :
        db_table = 'EN_PAIS'
        constraints = [
            models.UniqueConstraint(fields=['cod_pais'], name='EN_PAIS_PK')
            # LLAVES FORANEAS

        ]



