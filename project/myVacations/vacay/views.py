from __future__ import print_function

from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.auth.models import User

from googleapiclient.discovery import build
from httplib2 import Http
import google.oauth2.credentials


import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request




# from oauth2client import file, client, tools

# Create your views here.
def myVacay(request):
    print(request.user)
    destinations=Destination.objects.filter(poster=request.user)
    print("you are in my vacay")
    place_ids=[]
    for destination in destinations:
        place_ids.append(destination.place_id)
    
    context={'destinations':destinations,
    'place_ids':place_ids
    }
    print("context:", context)
    
    return render(request,"vacay/myVacay.html",context)

def myGallery(request,destination_id):
    print(destination_id)
    destination=Destination.objects.get(id=destination_id)
    print(destination.name)
    context={'destination':destination}
    return render(request,"vacay/myGallery.html",context)

def newDestination(request):
 
    return render(request,"vacay/newDestination.html")

def add_destination(request):

    
    # place_id=models.CharField(max_length=2    55) 
    # name=models.CharField(max_length=255) 
    # from_date=models.DateField()
    # to_date=models.DateField()
    # description=models.TextField()
    # album_title=models.CharField(max_length=255) 
    # album_cover=models.ImageField(default='default.jpg',upload_to='images')
    # poster=models.ForeignKey(Us

    print("name:",request.POST['name']),request.FILES['album_cover']
    print(request.POST['from_date'],request.FILES['album_cover'])
    print(request.POST['place_id'],"AID*****:", request.POST['AlbumId'])
    
    # errors=Destination.objects.valid_show(request.POST)
    # if len(errors)>0:
    #     print(errors)
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect("newDestination")

    user=User.objects.get(username=request.user.username)
    print(f"Add this location to this user {user.username}")
 

    new_destination=Destination.objects.create(place_id=request.POST['place_id'], name=request.POST['name'],from_date=request.POST['from_date'],to_date=request.POST['to_date'],description=request.POST['description'],album_title=request.POST['album_title'],album_url=request.POST['AlbumUrl'],album_id=request.POST['AlbumId'],album_cover=request.FILES['album_cover'],poster=user)
    print(f"Add this location to this user {new_destination.name}, {user.username}")
    # print(new_show.poster)
    return redirect("myVacay")

def Gallery(request):
    return render(request,"vacay/Gallery.html")
def Albums(request):
    return render(request,"vacay/Albums.html")
