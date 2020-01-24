from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    fuel = models.CharField(max_length=20)
    modeli = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    year_model = models.CharField(max_length=20)
    drive = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(
        default='default.jpg', upload_to='image_jobbs', blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(max_length=20)
    address = models.CharField(help_text='Address', max_length=60)
    city = models.CharField(help_text='City', max_length=40)
    country = models.CharField(help_text='Country', max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    
