
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone 
# from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    caption = models.TextField() 
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
          return self.caption

class Profile(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    picture = models.ImageField(blank=True,null=True)
    bio  =  models.TextField(null=True)
    
    
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
         return self.body[0:50]
      
      