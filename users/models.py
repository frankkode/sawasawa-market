from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.signals import request_finished
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in, user_signed_up
from PIL import Image
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #purchased_slots = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
