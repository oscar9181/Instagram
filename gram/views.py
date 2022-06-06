from multiprocessing import context
from django.shortcuts import render
from.models import Post
from django.contrib.auth.forms import UserCreationForm

from.forms import CreateUserForm


def registerPage(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        
        
    context = {'form':form}
    return render(request,'instagram/register.html',context)

def loginPage(request):
    context = {}
    return render(request,'instagram/login.html',context)



def insta(request):
    return render(request,'instagram/insta.html')