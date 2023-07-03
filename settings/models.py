from django.db import models
from django.utils import timezone
# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=60)
    logo = models.ImageField(upload_to='settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=300)
    fb_link = models.URLField(max_length=200)
    ins_link = models.URLField(max_length=200)
    tw_link = models.URLField(max_length=200)
    address = models.CharField(max_length=100)



    def __str__(self):
        return self.site_name


class NewsLatter(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.email