from django.db import models
from django.urls import reverse

# Create your models here.
class Plant(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  time = models.IntegerField()

  def __str__(self):
    return str(self.type)

  def get_absolute_url(self):
    return reverse('plants_details', kwargs={'plant_id': self.id})