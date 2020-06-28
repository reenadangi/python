from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('config/', views.stripe_config),  #new
    path('create-checkout-session/', views.create_checkout_session), # new

]
