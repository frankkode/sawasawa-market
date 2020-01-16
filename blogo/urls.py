from django.urls import path
from . import views
from .views import (blogo_index)




urlpatterns = [
    path("", views.blogo_index, name="blogo_index"),
    path("<int:pk>/", views.blogo_detail, name="blogo_detail"),
    path("<category>/", views.blogo_category, name="blogo_category"),
]