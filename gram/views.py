from multiprocessing import context
from django.shortcuts import render,redirect
from.models import Post, Profile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from.forms import CreateUserForm, NewPostForm

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def insta(request): 
    picture = Profile.objects.all()
    images = Post.objects.all()
    return render(request,'instagram/insta.html', {'images': images},{'picture': picture})



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('instagram')
    else:
      form=CreateUserForm()
      if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            
            return redirect('login')
        
    context = {'form':form}
    return render(request,'instagram/register.html',context)

def loginPage(request):
   
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('instagram')
        else:
           messages.info(request,'Username OR Password is incorrect')
       
    context = {}
    return render(request,'instagram/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        new_post = Post.objects.create(author=request.user, image=image, caption=caption)
        new_post.save()
        return redirect('instagram')
         
        
    return render(request,'instagram/NewPost.html')

def profile(request):
    
    profile = Profile.objects.get(user=request.user)
    
    return render(request,'instagram/profile.html',{'profile': profile})