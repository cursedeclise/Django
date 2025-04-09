from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('challenges/', views.challenges, name='challenges'),
]