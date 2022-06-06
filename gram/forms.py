from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms





class NewPostForm(forms.ModelForm):
        image = forms.ImageField(required=True)
        caption  = forms.CharField(widget=forms.Textarea(attrs={'class':'input is-medium'}),required=True)
        
        class Meta:
            model = Post
            field = ('image','caption')
            
            
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        field = ['username','email','password1','password2']