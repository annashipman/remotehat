from django.http import HttpResponse
from django.shortcuts import render

from .models import FamousNames

def index(request):
    return render(request, 'hat/index.html')

def add_names(request):
    return render(request, "hat/add_names.html")

def submit_name(request):
    try:
        famous_name = request.POST['famous_name']
        f = FamousNames(name_text=famous_name)
        f.save()
    except:
        # Not sure what error might be raised here
        # Worth noting that it allows empty strings to be submitted
        return render(request, 'hat/add_names.html', {
            'error_message': "An error occurred",
        })
    return render(request, 'hat/submit_name.html', {'famous_name': famous_name})

def retrieve_random_name(request):
    response = "random name chosen by dice roll"
    return HttpResponse(response)
