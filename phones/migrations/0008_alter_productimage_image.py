# Generated by Django 5.0.4 on 2024-06-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='static/product_images/'),
        ),
    ]
