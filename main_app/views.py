from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Plant, Photo
from .forms import CaringForm
import uuid
import boto3

S3_BASE_URL = "https://s3.us-east-2.amazonaws.com/"
BUCKET = 'thegardeningproject2'

# Create your views here.
class Home(LoginView):
  template_name='home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
  plants= Plant.objects.filter(user=request.user)
  return render(request, 'plants/index.html', { 'plants': plants })

@login_required
def plants_details(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  caring_form = CaringForm()
  return render(request, "plants/detail.html", { 
    "plant": plant, 
    "caring_form": caring_form
  })

class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = ['type', 'description', 'time']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['type', 'description', 'time']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url='/plants/'

@login_required
def add_caring(request, plant_id):
  form = CaringForm(request.POST)

  if form.is_valid():
    new_caring = form.save(commit=False)
    new_caring.plant_id = plant_id
    new_caring.save()
  return redirect('plants_details', plant_id=plant_id)
  
@login_required
def add_photo(request, plant_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, plant_id=plant_id)
      plant_photo = Photo.objects.filter(plant_id=plant_id)
      if plant_photo.first():
        plant_photo.first().delete()
      photo.save()
    except Exception as err:
      print("An error occurred uploading the file: %s" % err)
  return redirect("plants_details", plant_id=plant_id)

def signup(request):
    error_message=""
    if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('plants_index')
      else:
        error_message = "Invalid signup - try again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



