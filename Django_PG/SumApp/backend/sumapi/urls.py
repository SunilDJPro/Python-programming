from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate_sum, name = 'calculate_sum'),
]
