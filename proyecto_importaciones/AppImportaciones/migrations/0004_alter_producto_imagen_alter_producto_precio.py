# Generated by Django 5.0.3 on 2024-09-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppImportaciones', '0003_producto_descripcion_producto_imagen_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=100),
        ),
    ]
