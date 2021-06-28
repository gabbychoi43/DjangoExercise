from django.db import models


# Create your models here.


class Hospital(models.Model):
    id=models.IntegerField(primary_key=True)
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical=models.IntegerField()
    room=models.IntegerField()
    tel = models.TextField(max_length=15)
    address=models.TextField(max_length=100)
