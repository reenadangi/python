from django.http import HttpResponse
from time import gmtime, strftime
from django.shortcuts import render,redirect	# notice the import!
from django.utils.crypto import get_random_string
from .models import post

def home(request):
     # get blog data from post model
     context={'posts':post.objects.all()}
     print(context)
     return render(request, "home.html",context)

     # if request.method == "GET":
     #      unique_id = get_random_string(length=32)
     #      context = {
     #      "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
     #      }
     #      name="Reena"
     #      return render(request, "home.html",{'unique_id':unique_id,'name': name,'date':context})
     
     # if request.method == "POST":
     #    print(request.POST)
     #    request.session['first_name'] = request.POST['first_name']
     #    request.session['email'] = request.POST['email']

     #    return redirect("/")

def about(request):
      return render(request, "myblog/about.html")
        




# def index(request):
#     return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
     return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
     return HttpResponse("Lets create a new BLOG !!")  

def show(request,my_val):
     return HttpResponse(f"No of blogs {my_val}!") 

def edit(request,my_val):
     return HttpResponse(f"Lets edit {my_val}!") 

def delete(request,my_val):
     return HttpResponse(f"Are you sure you want to delete {my_val}?") 



    