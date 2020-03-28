from django.urls import path,include
from . import views

urlpatterns = [
      path('',views.home,name="gold_app_home"),
      path('process_money/',views.process_money,name="gold_process_money"),
      path('reset/',views.reset,name="gold_process_reset"),
]