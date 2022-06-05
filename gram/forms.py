from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
        image = forms.ImageField(required=True)
        caption  = forms.CharField(widget=forms.Textarea(attrs={'class':'input is-medium'}),required=True)
        
        class Meta:
            model = Post
            field = ('image','caption')