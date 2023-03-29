from django.db import models
from django.shortcuts import reverse

class Benefits(models.Model):
    image = models.ImageField('Фото')
    name = models.CharField('Название', max_length=255)
    desc = models.TextField('Описание')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Преимущества'

class Vacancy(models.Model):
    post = models.CharField('Должность', max_length=155)
    desc = models.TextField('Описание')
    location = models.CharField('Место', max_length=255)

    def __str__(self) -> str:
        return self.post
    
    class Meta:
        verbose_name_plural = 'Вакансии'

class Apply(models.Model):
    name = models.CharField('Ф.И.О', max_length=155)
    email = models.EmailField('email адрес')
    phone = models.CharField('Номер телефона', max_length=15)
    post = models.CharField('Должность', max_length=155)
    image = models.ImageField('Фото', upload_to='vacancy/')
    text = models.TextField('Текст')

    def __str__(self) -> str:
        return f'{self.name} | {self.post}'
    
    class Meta:
        verbose_name_plural = 'Заявки'
