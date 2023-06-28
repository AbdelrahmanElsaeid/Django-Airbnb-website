from django.db import models
from django.contrib.auth.models import User
#from utils.Generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', null=True, blank=True, default='default.png')
    phone_number = models.CharField(max_length=20 )
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)


@receiver(post_save,sender=User,)
def Create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)

