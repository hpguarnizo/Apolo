# Generated by Django 2.0.3 on 2018-04-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_auto_20180408_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='permiso',
            field=models.CharField(choices=[('Tiene permisos de super administrador', '1'), ('No tiene permiso', '0')], default='No tiene permiso', max_length=25),
        ),
    ]
