# Generated by Django 4.1.7 on 2023-03-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_slides_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='slides',
            name='service',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название услуги'),
        ),
    ]
