from django.conf.urls import url
from .views import (job_index)
from . import views

app_name='jobbs'

urlpatterns = [
    url(r'^$', views.job_index, name="job_index"),
    url(r'^(?P<id>[\w-]+)/$', views.job_detail, name="job_detail"),
]