from django.core.exceptions import ValidationError
from django.db import models


class Olympiads(models.Model):
    title = models.CharField(max_length=150, unique=True, help_text="с большой буквы", verbose_name='Название олимпиады')
    short_name = models.CharField(max_length=50, help_text="с большой буквы", verbose_name='Сокращенное название')
    link = models.CharField(max_length=150, verbose_name='Ссылка')

    def clean(self):
        if ord(self.title[0]) < 1040 or ord(self.title[0]) > 1071:
            raise ValidationError("Название олимпиады должно начинаться с большой буквы")
        if len(self.short_name) > 0 and (ord(self.short_name[0]) < 1040 or ord(self.short_name[0]) > 1071):
            raise ValidationError("Сокращенное название олимпиады должно начинаться с большой буквы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Олимпиада'
        verbose_name_plural = 'Олимпиады'


class Stages(models.Model):
    title = models.CharField(max_length=150, unique=True, help_text="с большой буквы без слова этап", verbose_name='Название этапа')

    def clean(self):
        if ord(self.title[0]) < 1040 or ord(self.title[0]) > 1071:
            raise ValidationError("Название этапа должно начинаться с большой буквы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'


class Timetable(models.Model):
    olympiad = models.ForeignKey('Olympiads', on_delete=models.CASCADE, verbose_name='Олимпиада')
    stage = models.ForeignKey('Stages', on_delete=models.CASCADE, verbose_name='Этап')
    date_interval = models.CharField(max_length=150, help_text="дата, месяц без года или 'пока не известно'", verbose_name='Даты проведения')
    start_date = models.DateField(help_text="дата-месяц-год", verbose_name='Начало этапа', blank=True, null=True)
    finish_date = models.DateField(help_text="дата-месяц-год", verbose_name='Окончание этапа', blank=True, null=True)
    finished = models.BooleanField(default=False, verbose_name='Завершилась')

    class Meta:
        verbose_name = 'Расписание'
        unique_together = ('olympiad', 'stage', 'start_date', 'finish_date')


class Materials(models.Model):
    olympiad = models.ForeignKey('Olympiads', on_delete=models.CASCADE, verbose_name='Олимпиада')
    stage = models.ForeignKey('Stages', on_delete=models.CASCADE, verbose_name='Этап')
    year = models.CharField(max_length=15, help_text="например 2000-2001", verbose_name='Год проведения')
    study_year = models.IntegerField(help_text="с 7 по 11", verbose_name='Класс')
    task = models.CharField(max_length=150, help_text="ссылка", verbose_name='Условия')
    task_title = models.CharField(max_length=150, help_text="возможные варианты: у у(7-9) у-р у-о и др. по ситуации", verbose_name='Название для таблицы', default='у')
    solution = models.CharField(max_length=150, verbose_name='Решения', blank=True)
    solution_title = models.CharField(max_length=150, help_text="возможные варианты: р р(7-9) и др. по ситуации", verbose_name='Название для таблицы', blank=True)

    def clean(self):
        if self.study_year > 11 or self.study_year < 7:
            raise ValidationError("Значение класса должно быть от 7 до 11")

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        unique_together = ('olympiad', 'stage', 'year', 'study_year', 'task', 'solution')


class News(models.Model):
    news_content = models.CharField(max_length=150, verbose_name='Контент новости')
    show = models.BooleanField(default=True, verbose_name='Отобразить')

    def clean(self):
        if ord(self.news_content[0]) < 1040 or ord(self.news_content[0]) > 1071:
            raise ValidationError("ННовость должна начинаться с большой буквы")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
