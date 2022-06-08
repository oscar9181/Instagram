from django.urls import path
from . import views



urlpatterns = [
     path('',views.insta,name='instagram'),
    
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('NewPost/',views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('comment/<int:pk>/',views.posted,name='add_comment')
    
]

