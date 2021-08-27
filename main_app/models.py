from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
CARES = (
  ('W', 'Watering'),
  ('P', 'Pruning'),
  ('F', 'Fertilizing')
)

class Plant(models.Model):
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  time = models.IntegerField()

  def __str__(self):
    return str(self.type)

  def get_absolute_url(self):
    return reverse('plants_details', kwargs={'plant_id': self.id})
    
class Gardening(models.Model):
  date = models.DateField('Gardening Date')
  care = models.CharField(max_length=1,
    choices=CARES,
    default=CARES[0][0]
  )
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_care_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  cat = models.OneToOneField(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for plant_id: {self.plant_id} @{self.url}"