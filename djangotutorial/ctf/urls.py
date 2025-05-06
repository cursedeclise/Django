from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('challenges/', views.challenges, name='challenges'),
    path('participants/', views.participants, name='participants'),
    path('challengeform/', views.challengesform, name='challengesform'),
    path('submitFlag/', views.submit_flag, name='submitFlag'),
    path('challenges/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('start_challenge/<int:challenge_id>/', views.start_challenge, name='start_challenge')
]