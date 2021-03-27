from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register(request):
    # if User.objects.filter(email=form.cleaned_data.get('email')).exists():

    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}, you can login now')
            print("*"*40,messages)
            return redirect("register")
    else:
        form=UserRegisterForm()
        # login_form=auth_views.LoginView.as_view()
        
    login_form = AuthenticationForm()
    context={'form':form,'login_form':login_form}
    return render(request,'users/register.html',context)

def signin(request):
    print("in login****")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("home")
            else:
                messages.warning(request, "Invalid username or password.")
        else:
            messages.warning(request, "Invalid username or password.")
    return redirect('register')
    
def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('register')

