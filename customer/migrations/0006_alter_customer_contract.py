# Generated by Django 5.1.6 on 2025-02-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_customer_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contract',
            field=models.DateField(null=True, verbose_name='Sözleşme Tarihi'),
        ),
    ]
