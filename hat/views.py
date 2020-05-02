from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'hat/index.html')

def add_names(request):
    return render(request, "hat/add_names.html")

def submit_name(request):
    famous_name = "Anna Shipman"
    return render(request, 'hat/submit_name.html', {'famous_name': famous_name})

def retrieve_random_name(request):
    response = "random name chosen by dice roll"
    return HttpResponse(response)
