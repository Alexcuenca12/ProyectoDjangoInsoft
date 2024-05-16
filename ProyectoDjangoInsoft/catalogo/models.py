from django.db import models

from BaseModelo.models import BaseModel


# Create your models here.
class EnTipoCatalogo(BaseModel):
    cod_tipo_catalogo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)

    class Meta:
        db_table = 'EN_TIPO_CATALOGO'
        constraints = [
            models.UniqueConstraint(fields=['cod_tipo_catalogo'], name='EN_TIPO_CATALOGO_PK')
        ]


class en_catalogo(BaseModel):
    cod_catalogo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    cod_tipo_catalogo = models.ForeignKey(EnTipoCatalogo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'EN_CATALOGO'
        constraints = [
            models.UniqueConstraint(fields=['cod_catalogo'], name='EN_CATALOGO_PK')
        ]
class EnCatalogoEmpresa(models.Model):
    cod_empresa = models.CharField(max_length=8)
    cod_catalogo = models.ForeignKey(en_catalogo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    cod_tipo_catalogo = models.ForeignKey(EnTipoCatalogo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'EN_CATALOGO_EMPRESA'
        constraints = [
            models.UniqueConstraint(fields=['cod_catalogo', 'cod_empresa'], name='EN_CATALOGO_X_EMPRESA_PK')
            # llaves fkcompuestas
        ]