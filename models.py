from __future__ import unicode_literals
from django.db import models
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["name"] = "Your name must be greater than 2 characters!"
        if len(postData['last_name']) < 2:
            errors["desc"] = "Your last name must be greater than 2 characters!"
        email = postData["email"]
        if '@' not in email:
            errors["email"] = "Your email must be a valid email!"
        return errors
        #This validator simply checks the above if statements and ensures that the loginreg forms are adequitly met before proceeding to the URL

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    passwordc = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()