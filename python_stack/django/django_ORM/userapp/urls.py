from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="userapp_home" ),
    path('add_user/', views.add_user,name="userapp_add_user" ),
    path('addnew/', views.addnew,name="userapp_adduser" ),
    path('update_user/<user_id>', views.update_user,name="userapp_update_user_id" ),
    path('update/', views.update,name="userapp_update" ),
    
]