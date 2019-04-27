from django.conf.urls import include, url
from django.contrib import admin
from api.views import *

urlpatterns = [
	url(r'^$', messageList.as_view()),
	url(r'^(?P<message_id>\w+)/$', getMessage.as_view()),
]
