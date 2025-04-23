from django.shortcuts import render
from .models import *
from django.contrib import messages

from .forms import *
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
        form=ChallengeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Challenge Submitted!")
            return render(request, 'challengeform.html', {'form':form, 'success': True})
    else:
        form = ChallengeForm()
    return render(request, 'challengeform.html', {'form':form})


def participants(request):
    participants=Participant.objects.all()


    return render(request, 'participant.html',{
        'participants': participants,
    }) 