# Generated by Django 2.0.3 on 2018-04-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0007_auto_20180408_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='permiso',
            field=models.CharField(choices=[('1', 'Tiene permisos de super administrador'), ('0', 'No tiene permiso')], default='No tiene permiso', max_length=85),
        ),
    ]