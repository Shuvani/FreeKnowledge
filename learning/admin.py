from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SectionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Sections, SectionsAdmin)


class TopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Topics, TopicsAdmin)


class VideosAdminForm(forms.ModelForm):
    theory = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Videos
        fields = '__all__'


class VideosAdmin(admin.ModelAdmin):
    form = VideosAdminForm
    list_display = ('id', 'section', 'topic', 'study_year', 'video_link')
    list_display_links = ('id', 'section', 'topic', 'study_year')


admin.site.register(Videos, VideosAdmin)


class TasksAdminForm(forms.ModelForm):
    task = forms.CharField(widget=CKEditorUploadingWidget())
    solution = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tasks
        fields = '__all__'


class TasksAdmin(admin.ModelAdmin):
    form = TasksAdminForm
    list_display = ('id', 'section', 'topic', 'study_year', 'task', 'image', 'answer', 'solution', 'video_solution_link')
    list_display_links = ('id', 'section', 'topic', 'study_year')


admin.site.register(Tasks, TasksAdmin)
