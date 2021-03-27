from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description=models.TextField(default="desc")
    uploaded_by =models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like =models.ManyToManyField(User, related_name="liked_books")
