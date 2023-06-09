# Generated by Django 4.1.7 on 2023-03-20 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='about/', verbose_name='Фото 1')),
                ('image2', models.ImageField(upload_to='about/', verbose_name='Фото 2')),
                ('image3', models.ImageField(upload_to='about/', verbose_name='Фото 3')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('video', models.CharField(max_length=255, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
