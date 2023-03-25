# Generated by Django 4.1.7 on 2023-03-20 17:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='blog/', verbose_name='Главное фото')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('slug', models.SlugField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='Фото')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogs', verbose_name='Блог')),
            ],
            options={
                'verbose_name_plural': 'Фото',
            },
        ),
    ]
