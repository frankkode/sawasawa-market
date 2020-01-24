from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete


class Post(models.Model):
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(help_text='Address', max_length=60)
    city = models.CharField(help_text='City', max_length=40)
    country = models.CharField(help_text='Country', max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='image_main_post')


    class Meta:
        ordering = ['-id']
        

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})


    def __str__(self):
            return str(self.title)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        default='default.jpg', upload_to='image_post', blank=True, null=True)
    

    def __str__(self):
            return str(self.post.id)

