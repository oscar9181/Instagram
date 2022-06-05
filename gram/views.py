from django.shortcuts import render
from.models import Post

# Create your views here.

def insta(request):
    return render(request,'instagram/insta.html')