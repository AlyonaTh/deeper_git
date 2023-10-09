from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('random_number/', views.random_number, name='random_number'),
]