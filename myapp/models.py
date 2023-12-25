from django.db import models




class practis(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField( max_length=50)
    compony=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    pin=models.CharField( max_length=50)