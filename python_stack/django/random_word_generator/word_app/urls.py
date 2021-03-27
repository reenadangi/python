from django.urls import path
from . import views
urlpatterns = [
	path('', views.rand_word,name="rand_word"),
    path('test',views.test),
    path('reset/',views.reset),
]
