from django.db import models

# Create your models here.



class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goals = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')



    def __str__(self) -> str:
        return str(self.id)


class FAQ(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField(max_length=3000)


    def __str__(self):
        return self.title