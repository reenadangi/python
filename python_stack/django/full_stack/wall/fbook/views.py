from django.shortcuts import render,redirect
from .models import Messages,Comments
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    msgs=Messages.objects.all().order_by("-created_at")
    context={'msgs':msgs}
    return render(request,"fbook/home.html",context)

def postmsg(request):
    msg=Messages.objects.create(message=request.POST["msgbox"],content=request.POST["msgbox"],poster=request.user,created_at="1199-12-12")
    print(msg)
    return redirect("home")

def postcomment(request):
    comment=Comments.objects.create(comment=request.POST['comment'],comment_by=request.user,comment_at=Messages.objects.get(id=request.POST["msg"]))
    return redirect("home")

def my_msgs(request,id):
    poster=User.objects.get(id=id)
    context={
        'the_user':poster
    }
    print(context)
    return render(request,"fbook/my_msgs.html",context)

def delete_msg(request,id):
    msg=Messages.objects.get(id=id)
    print(f"delete this message{id},{msg.message}")
    msg.delete()
    return redirect("home")