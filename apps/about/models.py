from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class About(models.Model):
    image1 = models.ImageField('Фото 1', upload_to='about/')
    image2 = models.ImageField('Фото 2', upload_to='about/')
    image3 = models.ImageField('Фото 3', upload_to='about/')
    text = RichTextField('Текст')
    video = models.CharField('Ссылка на видео', max_length=255)

    def __str__(self) -> str:
        return 'О нас'
    
    class Meta:
        verbose_name_plural = 'О нас'