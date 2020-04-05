from django.contrib import admin
from .models import Listing
# from .models import Realtor

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','realtor')
    
# Register your models here.
admin.site.register(Listing)
# admin.site.register(Realtor)
