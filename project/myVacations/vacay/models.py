from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class destinationManager(models.Manager):
    def valid_show(self,postData):
        errors={}
        if len(postData['name'])<2:
           errors["short"]="Show name should be more than 2 char"

    

class Destination(models.Model):
    place_id=models.CharField(max_length=255) 
    name=models.CharField(max_length=255) 
    from_date=models.DateField()
    to_date=models.DateField()
    description=models.TextField()
    album_title=models.TextField()
    album_cover=models.ImageField(default='default.jpg',upload_to='images')
    album_url=models.TextField()
    album_id=models.TextField(default='none')
    poster=models.ForeignKey(User,related_name="destinations", on_delete=models.CASCADE)
    objects=destinationManager()