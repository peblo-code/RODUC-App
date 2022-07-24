# Generated by Django 3.2.7 on 2022-06-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoducWeb', '0024_recursos_auxiliar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Eva',
            fields=[
                ('cod_tipo_eva', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]