from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext as _

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    tags = TaggableManager()
    image = models.ImageField(_("image"),upload_to='post/')
    create_at = models.DateTimeField( _('title'), default=timezone.now)
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE, verbose_name=_('author'))
    description = models.TextField(_('description'),max_length=15000)
    category = models.ForeignKey('Category', related_name='post_category' ,on_delete=models.CASCADE,verbose_name=_('category'))
    slug = models.SlugField( _('url'),null=True,blank=True)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)  

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100)  


    
    def __str__(self):
        return self.name


