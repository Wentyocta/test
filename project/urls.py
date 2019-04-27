from django.conf.urls import include, url
from django.contrib import admin
from api.views import *

urlpatterns = [
    url(r'^api/', include('api.urls')),
]
