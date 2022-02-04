from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    age = models.IntegerField()
    occupation = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/', verbose_name='Photo', null=True)
