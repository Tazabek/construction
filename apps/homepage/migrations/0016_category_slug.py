# Generated by Django 4.1.7 on 2023-03-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_alter_projects_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
