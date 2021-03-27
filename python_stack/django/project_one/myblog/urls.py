from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='myblog-home'),
    path('about/', views.about, name='myblog-about'),

    path('new/', views.new, name='myblog-new'),
    path('create/', views.create, name='myblog-create'),
    path('<>/edit', views.edit, name='myblog-edit'),


]

# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^new$', views.new),
#     url(r'^create$', views.create),
#     url(r'^(?P<my_val>\d+)$', views.show),
#     url(r'^(?P<my_val>\d+)/edit$', views.edit),
#     url(r'^(?P<my_val>\d+)/delete$', views.delete),
# # r'^bears/(?P<my_val>\d+)$'
# ]