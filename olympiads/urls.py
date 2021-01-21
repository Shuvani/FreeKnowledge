from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', timetable),
    url(r'^materials/(?P<grade>[7-9]{1}|[1]{1}[0-1]{1})/$', materials, name='materials'),
]