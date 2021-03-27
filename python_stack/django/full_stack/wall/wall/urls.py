"""wall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from fbook import views as fbook_views

# Django provides login and logout views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.register,name="register"),
    path('signin/', user_views.signin, name="signin"),
    path('signout/',user_views.signout,name="signout"),

    path('home/',fbook_views.home,name="home"),
    path('postmsg/',fbook_views.postmsg,name="postmsg"),  
    path('postcomment/',fbook_views.postcomment,name="postcomment"),  
    path('my_msgs/<int:id>/',fbook_views.my_msgs,name="my_msgs"),  
    path('delete_msg/<int:id>/',fbook_views.delete_msg,name="delete_msg"),  
    
    

    
    

    

   
]
