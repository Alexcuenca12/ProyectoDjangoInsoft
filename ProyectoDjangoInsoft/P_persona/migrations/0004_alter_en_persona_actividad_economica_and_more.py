# Generated by Django 5.0.6 on 2024-05-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P_persona', '0003_en_catalogo_audit_fecha_ing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='en_persona',
            name='ACTIVIDAD_ECONOMICA',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='ACTIVIDAD_ECONOMICA'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='CLASE_CONTRIBUYENTE',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='CLASE_CONTRIBUYENTE'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='CODIGO_REFERENCIA',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CODIGO_REFERENCIA'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='FECHA_ESTABLECIDO_NEGOCIO',
            field=models.DateField(blank=True, null=True, verbose_name='FECHA_ESTABLECIDO_NEGOCIO'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='FECHA_INICIO_ACTIVIDAD_ECON',
            field=models.DateField(blank=True, null=True, verbose_name='FECHA_INICIO_ACTIVIDAD_ECON'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='NOMBRE_ARRENDATARIO_LOCAL',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='NOMBRE_ARRENDATARIO_LOCAL'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='NOMBRE_ARRENDATARIO_VIVIENDA',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='NOMBRE_ARRENDATARIO_VIVIENDA'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='NOMBRE_COMERCIAL',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='NOMBRE_COMERCIAL'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='NRO_HIJOS',
            field=models.IntegerField(blank=True, null=True, verbose_name='NRO_HIJOS'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='NUM_CARGAS',
            field=models.IntegerField(blank=True, null=True, verbose_name='NUM_CARGAS'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='OBLIGADO_CONTRIBUYENTE',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='OBLIGADO_CONTRIBUYENTE'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='OBSERVACIONES',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='OBSERVACIONES'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='SEPARACION_BIENES',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='SEPARACION_BIENES'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='TELEFONO_ARRENDATARIO_LOCAL',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='TELEFONO_ARRENDATARIO_LOCAL'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='TELEFONO_ARRENDATARIO_VIVIENDA',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='TELEFONO_ARRENDATARIO_VIVIENDA'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='TIPO_LOCAL',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='TIPO_LOCAL'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='TIPO_PERSONA_SRI',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='TIPO_PERSONA_SRI'),
        ),
        migrations.AlterField(
            model_name='en_persona',
            name='TIPO_VIVIENDA',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='TIPO_VIVIENDA'),
        ),
    ]