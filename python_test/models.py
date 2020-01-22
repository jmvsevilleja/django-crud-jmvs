from django.db import models

# Insert models here

# create a model to store a "Client"


class Client(models.Model):

    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
