from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from apps.homepage.models import Category

class Services(models.Model):
    image = models.ImageField('Фото', upload_to='service/')
    name = models.CharField('Название услуги', max_length=255, blank=True, null=True)
    text = RichTextField('Описание')
    slug = models.SlugField('Ссылка')
    number = models.CharField('Номер', max_length=15, default='', blank=True, null=True)
    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse("single_service", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f'{self.name} | {self.id}'
    
    class Meta:
        verbose_name_plural = 'Услуги'


class Advertisement(models.Model):
    image = models.ImageField('Фото', upload_to='service/')
    text = RichTextField('Текст')

    def __str__(self) -> str:
        return 'Об услугах'
    
    class Meta:
        verbose_name_plural = 'Об услугах'
