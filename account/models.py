from django.db import models

# Create your models here.
class person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    number = models.IntegerField() 
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    State = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isactive = models.BooleanField(default=True)
class notification(models.Model):
    notification = models.CharField(max_length=500)

