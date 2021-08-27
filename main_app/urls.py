from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('plants/', views.plants_index, name='plants_index'),
    path("plants/<int:plant_id>/", views.plants_details, name="plants_details"),
    path("plants/create/", views.PlantCreate.as_view(), name="plants_create"),
    path("plants/<int:pk>/update/", views.PlantUpdate.as_view(), name="plants_update"),
    path("plants/<int:pk>/delete/", views.PlantDelete.as_view(), name="plants_delete"),
    path("plants/<int:plant_id>/add_caring/", views.add_caring, name='add_caring'),
    path('plants/<int:plant_id>/add_photo/', views.add_photo, name="add_photo"),
    # path('accounts/signup/', views.signup, name="signup")
]