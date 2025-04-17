from django.shortcuts import render
from .models import *
from django.contrib import messages

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

def challengesform(request):
    if request.method == 'POST':
        form=challengesform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'challengesform.html', {'form':form, 'success': True})


def participants(request):
    participants=Participant.objects.all()


    return render(request, 'participant.html',{
        'participants': participants,
    })