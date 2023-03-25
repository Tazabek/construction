from django.db import models

class History(models.Model):
    year = models.CharField('Года', max_length=15)
    name = models.CharField('Название событии', max_length=255)
    desc = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='history/')

    def __str__(self) -> str:
        return f'{self.year} | {self.name}'
    
    class Meta:
        verbose_name_plural = 'Наша история'
