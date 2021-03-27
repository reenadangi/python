from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# one to many relationship

# Create your models here.
class Messages(models.Model):
    message=models.TextField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # if user is deleted delete their post too !
    poster=models.ForeignKey(User,related_name="messages", on_delete=models.CASCADE) 

# one to many relationship
class Comments(models.Model):
    comment=models.TextField()
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    # if user is deleted delete their post too !
    comment_by=models.ForeignKey(User,related_name="user_comments", on_delete=models.CASCADE)
    comment_at=models.ForeignKey(Messages, related_name="msg_comments", on_delete=models.CASCADE)
