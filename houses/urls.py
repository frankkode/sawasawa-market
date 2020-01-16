from django.conf.urls import url
from .views import (house_index)
from . import views

app_name='houses'

urlpatterns = [
    url(r'^$', views.house_index, name="house_index"),
    url(r'^(?P<id>[\w-]+)/$', views.house_detail, name="house_detail"),
]