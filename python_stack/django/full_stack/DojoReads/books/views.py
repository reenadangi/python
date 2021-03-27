from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth.models import User
import json

# Create your views here.

def home(request):
    context={'books':Book.objects.all().filter(uploaded_by_id=request.user.id)}
    print(f"##### {request.user.username},{context}")
    return render(request,"books/home.html",context)

def add(request):
    
    print("in add", request.POST["title"],request.user.id)
    # results = {}
    # for key, value in request.session.items():
    #     print("this is dict",key,value)
    #     results[key]=value
    # print(results)
    # result = json.dumps(results)
    # print ("\n", type(result)) 
    # print ("final string = ", result) 
    

    if request.method=="POST":         
        book=Book.objects.create(title=request.POST["title"],description=request.POST["description"],uploaded_by=User.objects.get(id=request.POST["user_id"]))
        print("added!")
    
    context={'books':Book.objects.all().filter(uploaded_by_id=request.user.id)}
    print(f"#####{context}")
    return redirect("books_home")



