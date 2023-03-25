from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from apps.homepage.models import Category


class Projects(models.Model):
    name = models.CharField('Название', max_length=155)
    main_image = models.ImageField('Фото', upload_to='project/')
    client = models.CharField('Клиент', max_length=255)
    date = models.DateField('Дата', auto_now=False, auto_now_add=False)
    adress = models.CharField('Адрес', max_length=255)
    slug = models.SlugField('Ссылка')
    desc = RichTextField(verbose_name='Описание')
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse("single_project", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Проекты'

class ProjectImages(models.Model):
    image = models.ImageField('Фото', upload_to='project/')
    project = models.ForeignKey(Projects, models.CASCADE, verbose_name='Проект')

    def __str__(self) -> str:
        return 'Фото'
    
    class Meta:
        verbose_name_plural = 'Фото проектов'