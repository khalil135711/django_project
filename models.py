from django.db import models

class newLesen(models.Model):
    num=models.IntegerField()
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=5000)