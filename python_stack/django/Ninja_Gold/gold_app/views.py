from django.shortcuts import render,redirect
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # context ="Ninja Gold App"
    
    return render(request,'gold_app/home.html')

def process_money(request):
    # context ="Ninja Gold App"
   if request.method == "POST":
        print(f"A POST request is being made to this route {request.POST['which']}")

        if request.POST['which'] == 'farm':
            gold=random.randint(10, 20)
        if request.POST['which'] == 'cave':
            gold=random.randint(5, 10)
        if request.POST['which'] == 'house':
            gold=random.randint(2, 5)
        if request.POST['which'] == 'casino':
            gold=random.randint(-50, 50)
        if ('gold' in request.session):
            print(request.session['gold'],"*"*50)
            request.session['gold'] = gold+int(request.session['gold'])
            # adding activities 
            activities=f"Earned {gold} from {request.POST['which']}"
            request.session['activities'].append(activities)
            print(request.session['activities'],"*"*80)
            
            request.session['moves']=int(request.session['moves'])-1
            if int(request.session['moves'])==0 and int(request.session['gold'])!= int(request.session['goal']):
                request.session['enable_game']=False
                request.session['won']=False
                activities=f"Your moves are over, GOLD: {request.session['gold']} , GOAL: {request.session['goal']} YOU LOST ! PLAY AGAIN"
                # request.session['activities']=[]
                request.session['activities'].append(activities)
                return redirect("/")
            if int(request.session['moves'])==0 and int(request.session['gold'])== int(request.session['goal']):
                request.session['enable_game']=False
                request.session['won']=True

                activities=f"YOU WON!!"
                # request.session['activities']=[]
                request.session['activities'].append(activities)
                return redirect("/")
            
        else:
            # request.session['activities']=[]
            request.session['gold'] = gold
            activities=f"Earned {gold} from {request.POST['which']}"
            request.session['activities'].append(activities) 
        return redirect("/")
        # return redirect("gold_app/process_money.html")

def reset(request):
    request.session['enable_game']=True
    request.session['gold']=0
    request.session['activities']=[]
    request.session['moves']=request.POST['moves']
    request.session['goal']=request.POST['goal']
    
    return redirect("/")



    