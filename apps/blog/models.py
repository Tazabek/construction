from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from apps.homepage.models import Category

class Blogs(models.Model):
    main_image = models.ImageField('Главное фото', upload_to='blog/')
    title = models.CharField('Название', max_length=255)
    text = RichTextField('Текст')
    slug = models.SlugField('Ссылка')
    date = models.DateField('Дата', auto_now_add=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    count = models.IntegerField('Счет', default=0)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        ordering = ('-id',)
    
class Images(models.Model):
    image = models.ImageField('Фото', upload_to='blog/')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name='Блог')

    def __str__(self) -> str:
        return f'Фото | {self.blog.title}'
    
    class Meta:
        verbose_name_plural = 'Фото'

class Commenst(models.Model):
    name = models.CharField('Имя', max_length=155)
    comment = models.TextField('Коммент')
    news = models.ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name='Комменты', related_name='comments')

    def __str__(self) -> str:
        return f'{self.name} | {self.news.title}'
    
    class Meta:
        verbose_name_plural = 'Комменты'