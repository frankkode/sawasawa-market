from django.conf.urls import url
from .views import (car_index)
from . import views

app_name='cars'

urlpatterns = [
    url(r'^$', views.car_index, name="car_index"),
    url(r'^(?P<id>[\w-]+)/$', views.car_detail, name="car_detail"),
]