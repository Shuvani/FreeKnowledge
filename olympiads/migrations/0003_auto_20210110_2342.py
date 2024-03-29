# Generated by Django 3.1.5 on 2021-01-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0002_auto_20210110_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='solution',
            field=models.CharField(blank=True, max_length=150, verbose_name='Решения'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='solution_title',
            field=models.CharField(blank=True, default='р', help_text='возможные варианты: р р(7-9) и др. по ситуации', max_length=150, verbose_name='Название для таблицы'),
        ),
    ]
