# Generated by Django 3.2.7 on 2022-06-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoducWeb', '0028_alter_cabecera_planilla_cod_tipo_clase'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabecera_planilla',
            name='descripcion_adecuacion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]