from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Member(models.Model):
    post = models.CharField('Должность', max_length=55)
    image = models.ImageField('Фото', upload_to="experts/", height_field=None, width_field=None, max_length=None)
    name = models.CharField('ФИО', max_length=255)
    email = models.EmailField('Почта')
    tel_num = models.CharField('Номер тел.', max_length= 15)
    twitter = models.CharField('Твиттер', max_length=155, blank=True, null=True)
    facebook = models.CharField('фейсбок', max_length=155, blank=True, null=True)
    instagram = models.CharField('инстаграм', max_length=155, blank=True, null=True)
    office = models.CharField('Адрес офиса', max_length=255)
    slug = models.SlugField('Ссылка')
    ex_desc = models.TextField('Описание опытов', blank=True, null=True)
    post_desc = models.TextField('Описание должности')
    skill_desc = models.TextField('Описание скиллов', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("expert", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'Сотрудники'

class Skills(models.Model):
    skill_name = models.CharField('Название', max_length=155)
    percent = models.IntegerField('Процент владения', help_text='цифра от 1 до 100')
    member = models.ForeignKey(Member, models.CASCADE)
    
    def __str__(self):
        return 'Скиллы'
    
    class Meta:
        verbose_name_plural = 'Скиллы'

class Experience(models.Model):
    name = models.CharField('Название', max_length=255)
    years = models.CharField('Длительность', max_length=155)
    member = models.ForeignKey(Member, models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Опыт работы'