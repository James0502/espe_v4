# Generated by Django 2.0.2 on 2023-05-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplos', '0005_categoria_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('contacto', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]