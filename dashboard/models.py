from django.db import models

# Create your models here.
class Opexseoul(models.Model):
  regDate = models.DateField()
  restaurant = models.CharField(max_length=300)
  personnel = models.IntegerField()
  price = models.IntegerField()
  borough = models.CharField(max_length=500, default = '')





    


