from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def challenges(request):
    #get data
    challenges=challenge.objects.all()
    #send data as context var


    return render(request, 'challenges.html',{
        'challenges': challenges,
    })