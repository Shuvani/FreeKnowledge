from django.contrib import admin
from .models import *


class OlympiadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_name', 'link')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'short_name')


admin.site.register(Olympiads, OlympiadsAdmin)


class StagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Stages, StagesAdmin)


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'olympiad', 'stage', 'date_interval', 'start_date', 'finish_date', 'finished')
    list_display_links = ('id', 'olympiad', 'stage')
    list_filter = ('finished', 'olympiad')


admin.site.register(Timetable, TimetableAdmin)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'olympiad', 'stage', 'year', 'study_year', 'task', 'task_title', 'solution', 'solution_title')
    list_display_links = ('id', 'olympiad', 'stage')
    list_filter = ('olympiad', 'year', 'study_year')


admin.site.register(Materials, MaterialsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_content', 'show')
    list_display_links = ('id', 'news_content')
    list_filter = ('show',)


admin.site.register(News, NewsAdmin)
