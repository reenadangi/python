from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing
from listings.choices import price_choices,bedroom_choices,state_choices


# Create your views here.
def index(request):
    # order by list_date(latest show first)
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    page_listings=paginator.get_page(page)
    context={
        'listings': page_listings
    }
    return render(request,'listings/listings.html',context)

def  listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    # listing=get_object_or_404(Listing,pk=listing_id)     
    queryset_list=Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    context={
        #   'listing':listing,
          'state_choices':state_choices,
          'bedroom_choices':bedroom_choices,
          'price_choices':price_choices,
          'listings':queryset_list
     }
    return render(request,'listings/search.html',context)
