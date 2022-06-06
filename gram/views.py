from multiprocessing import context
from django.shortcuts import render
from.models import Post


def registerPage(request):
    context = {}
    return render(request,'instagram/register.html',context)

def loginPage(request):
    context = {}
    return render(request,'instagram/login.html',context)



def insta(request):
    return render(request,'instagram/insta.html')