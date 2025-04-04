from django.db import models

from config.settings import AUTH_USER_MODEL


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    picture = models.ImageField(blank=True, verbose_name='Превью')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True,
                              null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="курсы", related_name="lessons", null=True)
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(blank=True, verbose_name='Превью')
    link = models.CharField(max_length=100, verbose_name="Ссылка")
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец урока", blank=True,
                              null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

