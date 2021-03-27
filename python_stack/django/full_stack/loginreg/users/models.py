from django.db import models

# Create your models here.
from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 3:
            errors['fname'] = "Name must be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['lname'] = "Last name must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Must enter a valid email"
        if len(postData['password']) < 8:
            errors['pass'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pass'] = "Password and confirm password must match"
        return errors
  

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()
# Create your models here.
