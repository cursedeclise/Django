from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse

from .forms import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def challenges(request):
    challenges=Challenge.objects.all()
    participant=None
    solved_challenge_ids= []

    if request.user.is_authenticated:
        participant=Participant.objects.get(user=request.user)
        solved_challenge_ids=participant.flags_solved.values_list('id', flat=True)

        print(f"Participant:{participant}, Type: {type(participant)}")
        print(f"Solved Challenges: {solved_challenge_ids}")

    return render(request, 'challenges.html', {
        'challenges': challenges,
        'participant': participant,
        'solved_challenge_ids': solved_challenge_ids,
    })

def challenge_detail(request, challenge_id):
    challenge= get_object_or_404(Challenge, id=challenge_id)
    return render(request, 'challenge_detail.html', {'challenge': challenge})

def start_challenge(request, challenge_id):
    challenge= get_object_or_404(Challenge, id=challenge_id)
    participant, created = Participant.objects.get_or_create(user=request.user)

    completion, created=ChallengeCompletion.objects.get_or_create(
        participant=participant, challenge=challenge
    )

    if not completion.start_time:
        completion.start_time=timezone.now()
        completion.save()
        return JsonResponse({"status":"success", "message": "Challenge started!"})
    return JsonResponse({"status":"success", "message": "Challenge already started!"})



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

def submit_flag(request):
    if request.method == 'POST':
        form=FlagSubmissionForm(request.POST)
        if form.is_valid():
            flag_value=form.cleaned_data['flag_value']
            try:
                challenge=  Challenge.objects.get(flag_value=flag_value)
                participant= Participant.objects.get(user=request.user)

                completion, created = ChallengeCompletion.objects.get_or_create(
                    participant=participant, challenge=challenge
                )

                if not completion.start_time:
                    messages.error(request, "Start time is missing. Try resfreshing the challenge page.")
                    return redirect('submitFlag')

                if challenge not in participant.flags_solved.all():
                    participant.flags_solved.add(challenge)

                    participant.update_points()

                    completion.timestamp = timezone.now()
                    time_taken=completion.timestamp - completion.start_time
                    completion.save()

                    messages.success(request, f'Flag submitted! you earned {challenge.points} points.')
                else:
                    messages.error(request, 'You already submitted this flag!')
            except Challenge.DoesNotExist:
                messages.error(request, 'Invalid flag. please try again.')
    else:
        form=FlagSubmissionForm()

    return render(request, 'submit_flag.html', {'form': form})