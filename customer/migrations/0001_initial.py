# Generated by Django 5.1.6 on 2025-02-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200, verbose_name='Müşteri Adı')),
                ('contack_name', models.CharField(max_length=200, verbose_name='Kontak Kişi')),
                ('checked', models.BooleanField(default=False, verbose_name='Aktif-Pasif')),
            ],
        ),
    ]
