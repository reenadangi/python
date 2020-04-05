from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing

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
    return render(request,'listings/search.html')
