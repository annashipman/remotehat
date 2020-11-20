from django.shortcuts import render
import random

from .models import FamousNames, Rounds

def index(request):
    return render(request, 'hat/index.html')

def add_name(request):
    return render(request, "hat/add_name.html")

def play(request):
    return render(request, "hat/play.html")

def submit_name(request):
    try:
        famous_name = request.POST['famous_name']
        if famous_name:
            f = FamousNames(name_text=famous_name)
            f.save()
    except:
        # Not sure what error might be raised here
        return render(request, 'hat/add_name.html', {
            'error_message': "An error occurred",
        })
    return render(request, 'hat/submit_name.html', {'famous_name': famous_name})

def retrieve_random_name(request):
    current_round = Rounds.objects.get()
    guessed_name = request.POST.get("famous_name")
    if guessed_name:
        successful_guess = FamousNames.objects.filter(round_number=current_round.current_round, name_text = guessed_name)[0]
        successful_guess.round_number += 1
        successful_guess.save()

    if not FamousNames.objects.filter(round_number=current_round.current_round):
        famous_name = "No names left in hat! End of round {}".format(current_round.current_round)
        current_round.current_round +=1
        current_round.save()
        ## Note that the 'got it, next' button still appears and will make this all fall over
       ## So need to make it not fall over
    else:
        names_in_round = list(FamousNames.objects.filter(round_number=current_round.current_round))
        famous_name = random.choice(names_in_round).name_text
    return render(request, 'hat/retrieve_name.html', {'famous_name': famous_name})
