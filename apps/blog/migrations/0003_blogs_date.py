# Generated by Django 4.1.7 on 2023-03-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата'),
        ),
    ]