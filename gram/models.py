from distutils.command.upload import upload
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True)
    image = models.ImageField(blank=True,null=True)

class Post(models.Model):
    author = models.ForeignKey('gram.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    caption = models.TextField() 
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
          return self.caption
      

    
    
    

      