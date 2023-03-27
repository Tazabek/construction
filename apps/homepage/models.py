from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField('Название', max_length=155)
    slug = models.SlugField('Ссылка', blank=True, null=True)

    def get_url(self):
        return reverse("category", kwargs={"slug": self.slug})
    
    def get_url_blog(self):
        return reverse("blog_cats", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории'


class Settings(models.Model):
    logo = models.ImageField('Лого', upload_to='logo/')
    adress = models.CharField('Адрес', max_length=255)
    adr_link = models.CharField('Ссылка на карту', max_length=255)
    email = models.EmailField('Почта')
    tel_num = models.CharField('Телефон', max_length=55)
    facbook = models.CharField('Фейсбук', max_length=255)
    twitter = models.CharField('Твиттер', max_length=255)
    youtube = models.CharField('Ютуб', max_length=255)
    linkedin = models.CharField('Линкедин', max_length=255)
    work = models.CharField('Рабочее дни', max_length=255, default='Понедельник- Пятница')
    work_time = models.CharField('Время работы', max_length=255, default='9:00 - 18:00')

    def __str__(self) -> str:
        return 'Общее параметры'

    class Meta:
        verbose_name_plural = 'Настройки'

class Slides(models.Model):
    image = models.ImageField('Фото', upload_to='slide/')
    text = RichTextField()
    service = models.CharField('Название услуги', max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Слайд'
    
    class Meta:
        verbose_name_plural = 'Слайд'
    

class Messages(models.Model):
    name = models.CharField('Имя', max_length=155, help_text='Ваше имя')
    email = models.EmailField('Email', help_text='Email Address')
    text = models.TextField('Сообщение')

    def __str__(self) -> str:
        return f'{self.name} | {self.email}'
    
    class Meta:
        verbose_name_plural = 'Сообщения'
