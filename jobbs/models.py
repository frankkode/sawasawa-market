
from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='image_jobbs', blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(help_text='Address', max_length=60)
    city = models.CharField(help_text='City', max_length=40)
    country = models.CharField(help_text='Country', max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    
    
   # def get_absolute_url(self):
       # return reverse('jobbs:job_detail', args=[self.jobb_id])


    class Meta:
        ordering = ['-id']

    def __str__(self):
            return self.title

    