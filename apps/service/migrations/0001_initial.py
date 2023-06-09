# Generated by Django 4.1.7 on 2023-03-21 17:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service/', verbose_name='Фото')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name_plural': 'Об услугах',
            },
        ),
    ]
