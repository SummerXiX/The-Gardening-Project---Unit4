from django.forms import ModelForm
from .models import Gardening

class CaringForm(ModelForm):
  class Meta:
    model = Gardening
    fields = ['date', 'caring']