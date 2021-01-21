from django.db import models
from django.core.exceptions import ValidationError


class Sections(models.Model):
    title = models.CharField(max_length=150, help_text="с большой буквы", verbose_name='Название раздела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Topics(models.Model):
    title = models.CharField(max_length=150, help_text="с большой буквы", verbose_name='Название темы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Videos(models.Model):
    section = models.ForeignKey('Sections', on_delete=models.CASCADE, verbose_name='Раздел')
    topic = models.ForeignKey('Topics', on_delete=models.CASCADE, verbose_name='Тема')
    study_year = models.IntegerField(verbose_name='Класс')
    video_link = models.CharField(max_length=300, blank=True, verbose_name='Ссылка на видео')
    theory = models.TextField(verbose_name='Теоретический материал')

    def clean(self):
        if self.study_year > 11 or self.study_year < 1:
            raise ValidationError("Значение класса должно быть от 1 до 11")

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Tasks(models.Model):
    section = models.ForeignKey('Sections', on_delete=models.CASCADE, verbose_name='Раздел')
    topic = models.ForeignKey('Topics', on_delete=models.CASCADE, verbose_name='Тема')
    study_year = models.IntegerField(verbose_name='Класс')
    task = models.TextField(verbose_name='Задание')
    image = models.ImageField(upload_to='images/learning', verbose_name='Иллюстрация', blank=True, null=True)
    answer = models.CharField(max_length=500, verbose_name='Ответ')
    solution = models.TextField(blank=True, verbose_name='Решение')
    video_solution_link = models.CharField(max_length=300, blank=True, verbose_name='Видео разбор')

    def clean(self):
        if self.study_year > 11 or self.study_year < 1:
            raise ValidationError("Значение класса должно быть от 1 до 11")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
