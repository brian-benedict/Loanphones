# Generated by Django 5.0.4 on 2024-06-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/product_images/'),
        ),
    ]
