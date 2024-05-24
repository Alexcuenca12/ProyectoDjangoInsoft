from django.db import models

from BaseModelo.models import BaseModel


# Create your models here.
class EnGeo(models.Model):
    cod_pais = models.CharField(max_length=8)
    cod_lugar = models.CharField(primary_key=True, max_length=8)  # The composite primary key (cod_lugar, cod_pais) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=100)
    cod_org = models.ForeignKey('EnOrgGeo', models.DO_NOTHING, db_column='cod_org')
    cod_sri = models.CharField(max_length=8, blank=True, null=True)
    cod_pais_padre = models.CharField(max_length=8, blank=True, null=True)
    cod_lugar_padre = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_lugar_padre', blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_ing = models.DateField(blank=True, null=True)
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True)
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    cod_icl = models.CharField(max_length=20, blank=True, null=True)
    cod_icl_parroquia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_geo'
        unique_together = (('cod_lugar', 'cod_pais'),)





class EnPais(models.Model):
    cod_pais = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=60)
    codigo_telefono = models.CharField(max_length=10, blank=True, null=True)
    gentilicio = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_ing = models.DateField(blank=True, null=True)
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True)
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)
    codigo_sri = models.CharField(max_length=20, blank=True, null=True)
    convenio_doble_tributacion = models.CharField(max_length=2)
    certificado_origen = models.CharField(max_length=1, blank=True, null=True)
    certificado_euro = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_pais'





class EnOrgGeo(models.Model):
    cod_pais = models.ForeignKey('EnPais', models.DO_NOTHING, db_column='cod_pais')
    cod_org = models.IntegerField(primary_key=True)  # The composite primary key (cod_org, cod_pais) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=60)
    audit_usuario_ing = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_ing = models.DateField(blank=True, null=True)
    audit_ip_ing = models.CharField(max_length=20, blank=True, null=True)
    audit_usuario_mod = models.CharField(max_length=30, blank=True, null=True)
    audit_fecha_mod = models.DateField(blank=True, null=True)
    audit_ip_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'en_org_geo'
        unique_together = (('cod_org', 'cod_pais'),)
