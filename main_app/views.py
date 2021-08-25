from django.shortcuts import render

# Create your views here.
class Plant:
    def __init__(self, type, description, time):
        self.type = type
        self.description = description
        self.time = time

plants = [
  Plant('The tall plant', 'watering + trimming', 3),
  Plant('Lemon Tree', 'watering + fruit picking', 0),
  Plant('Passion Fruit Tree', 'watering + watching out for bears', 4),
  Plant('cactus', 'sunlight', 6)
]
        

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })





