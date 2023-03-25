# Generated by Django 4.1.7 on 2023-03-24 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commenst'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'ordering': ('-id',), 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='commenst',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogs', verbose_name='Комменты'),
        ),
    ]
