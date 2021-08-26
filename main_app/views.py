from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant
from .forms import CaringForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  plants= Plant.objects.all()
  return render(request, 'plants/index.html', { 'plants': plants })

# @login_required
def plants_details(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  # caring_form = CaringForm()
  return render(request, "plants/detail.html", { 
    "plant": plant, 
    # "feeding_form": feeding_form,
    # "toys": toys_finch_doesnt_have
  })

class PlantCreate(CreateView):
  model = Plant
  fields = ['type', 'description', 'time']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['type', 'description', 'time']

class PlantDelete(DeleteView):
  model = Plant
  success_url='/plants/'

def add_caring(request, plant_id):
  form = CaringForm(request.POST)

  if form.is_valid():
    new_caring = form.save(commit=False)
    new_caring.plant_id = plant_id
    new_caring.save()
  return redirect('plants_details', plant_id=plant_id)
  





