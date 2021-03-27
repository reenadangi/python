from django.shortcuts import render,redirect
from .models import Users
# Create your views here.
def home(request):
    # context={'posts':post.objects.all()}
    context={'users':Users.objects.all()}
    print(context)
    return render(request,"userapp/home.html",context)

def add_user(request):
    return render(request,"userapp/add_user.html")

def addnew(request):
    print("adding new user",request.POST['first_name'])
    new_user=Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email_address=request.POST['email'],age=request.POST['age'])
    print (new_user)
    return redirect("/")

def update_user(request,user_id):
    print("in update")
    update_user={'user':Users.objects.get(id=user_id)}
    # print (update_user.first_name,update_user.last_name)
    return render(request,"userapp/update_user.html", update_user)
   
def update(request):
    print("updated")
    user=Users.objects.get(id=request.POST['user_id'])
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email_address=request.POST['email']
    user.age=request.POST['age']
    user.save()
    return redirect("/")