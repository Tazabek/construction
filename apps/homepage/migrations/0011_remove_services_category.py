# Generated by Django 4.1.7 on 2023-03-18 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_alter_services_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='category',
        ),
    ]
