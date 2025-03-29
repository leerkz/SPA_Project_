from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    picture = models.ImageField(blank=True, verbose_name='Превью')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(blank=True, verbose_name='Превью')
    link = models.CharField(max_length=100, verbose_name="Ссылка")

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

