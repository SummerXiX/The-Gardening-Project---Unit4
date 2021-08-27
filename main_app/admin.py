from django.contrib import admin
from .models import Plant, Gardening, Photo

# Register your models here.
admin.site.register(Plant)
admin.site.register(Gardening)
admin.site.register(Photo)