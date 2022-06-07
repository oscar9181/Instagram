from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('NewPost/',views.post,name='post'),
     path('profile/',views.profile,name='profile'),
    
    path('',views.insta,name='instagram')
]

