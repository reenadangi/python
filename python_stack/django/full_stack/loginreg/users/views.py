from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    #validate post data
    if User.objects.filter(email=request.POST['email']).exists():
        errors="This email already taken"
        return redirect('/')
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #create user
    new_user = User.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        email=request.POST['email'], 
        password=request.POST['password'])
    # redirect to success
    request.session['user'] = new_user.id
    messages.error(request, "User created, please sign in to continue")
    return redirect('/success')

def login(request):
    #test if inputted email matches an email in db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user) > 0:
    #test if inputted password matches password from db
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].id
            return redirect('/success')
    messages.error(request, "Invalid sign in data")
    return redirect('/')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, "users/success.html")

def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.