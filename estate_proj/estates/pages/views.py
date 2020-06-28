from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtor.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices
import stripe

from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new



# Create your views here
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'car',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def index(request):
     
     print("inside index")
     listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
     context={
          'listings':listings,
          'state_choices':state_choices,
          'bedroom_choices':bedroom_choices,
          'price_choices':price_choices,

     }
     return render(request,'pages/index.html',context)

def about(request):
     realtors=Realtor.objects.order_by('-hire_date')
     # get seller of the month
     mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
     context={
          'realtors':realtors,
          'mvp_realtors':mvp_realtors
     }

     return render(request,'pages/about.html',context)