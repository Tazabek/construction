# Generated by Django 4.1.7 on 2023-03-18 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=55, verbose_name='Должность')),
                ('image', models.ImageField(upload_to='experts/', verbose_name='Фото')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('post_desc', models.TextField(verbose_name='Описание должности')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('tel_num', models.CharField(max_length=15, verbose_name='Номер тел.')),
                ('office', models.CharField(max_length=255, verbose_name='Адрес офиса')),
                ('slug', models.SlugField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'Технические эксперты',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('skill_name', models.CharField(max_length=155, verbose_name='Название')),
                ('percent', models.IntegerField(help_text='цифра от 1 до 100', verbose_name='Процент владения')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member')),
            ],
            options={
                'verbose_name_plural': 'Скиллы',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('years', models.CharField(max_length=155, verbose_name='Длительность')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.member', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name_plural': 'Опыт работы',
            },
        ),
    ]