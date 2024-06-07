from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from uuid import uuid4
from accounts.models import User
# from accounts.models import User

# Create your models here.
  

class Categories(models.Model):
    # auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,blank=True, null=True)
    image = models.ImageField(upload_to='images/categories/image/')
    content = models.TextField()
    timestamp = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = ('Categories')
        verbose_name_plural = ('Categories')


class Blog(models.Model):
    # auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,blank=True, null=True)
    image = models.ImageField(upload_to='images/blog/image/')
    content = models.TextField()
    timestamp = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    CATEGORY_CHOICES = (('software-developer', 'Software Developer'),('accounting', 'Accounting'))

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    course =models.CharField(max_length=128,choices=CATEGORY_CHOICES,default="software-developer")
    timestamp = models.DateTimeField(db_index=True,auto_now_add=True)


    def __str__(self):
        return str(self.name)
    