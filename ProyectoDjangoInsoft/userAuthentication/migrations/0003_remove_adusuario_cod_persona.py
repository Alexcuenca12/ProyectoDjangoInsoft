# Generated by Django 5.0.6 on 2024-05-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthentication', '0002_alter_adusuario_cod_persona_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adusuario',
            name='cod_persona',
        ),
    ]