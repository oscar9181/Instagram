
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
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    
    class Meta:
      ordering = ['-created']
    
    def __str__(self):
          return self.caption

class Profile(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    picture = models.ImageField(blank=True,null=True ,default='default.jpg')
    bio  =  models.TextField(null=True)
    
    
class Comment(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    
    
    class Meta:
      ordering = ['-created']
    
    def __str__(self):
         return self.body[0:50]

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
      
    def __str__(self):
        return self.username