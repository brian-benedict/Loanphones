# Generated by Django 5.0.4 on 2024-04-09 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_loanapplication_product_initial_loan_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='amount',
        ),
    ]
