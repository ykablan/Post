# Generated by Django 5.1.6 on 2025-02-17 11:33

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('checked', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer', verbose_name='müşteriler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'ordering': ['-publishing_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='İsim')),
                ('content', models.TextField(verbose_name='Yorum')),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
            options={
                'ordering': ['-publishing_date'],
            },
        ),
    ]
