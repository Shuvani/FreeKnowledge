from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<grade>[7-9]{1}|[1]{1}[0-1]{1})/$', learning_topics, name='learning_topics'),
    url(r'^content/(?P<content_id>\d+)/$', learning_content, name='learning_content'),
]