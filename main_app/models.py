from django.db import models

# Create your models here.
from django.db import models

class Plant(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  time = models.IntegerField()