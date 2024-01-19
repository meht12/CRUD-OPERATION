from django.db import models


class record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    city = models.CharField(max_length=15)
    state= models.CharField(max_length=15)
    country = models.CharField(max_length=20)

def __str__(self):
    return('Hello')


