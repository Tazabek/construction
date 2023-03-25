# Generated by Django 4.1.7 on 2023-03-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_settings_adr_link_alter_settings_facbook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='work',
            field=models.CharField(default='Понедельник- Пятница', max_length=255, verbose_name='Рабочее дни'),
        ),
        migrations.AddField(
            model_name='settings',
            name='work_time',
            field=models.CharField(default='9:00 - 18:00', max_length=255, verbose_name='Время работы'),
        ),
    ]
