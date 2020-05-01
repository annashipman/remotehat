from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Hat")

def submit_name(request):
    famous_name = "Anna Shipman"
    return HttpResponse("You've submitted: %s." % famous_name)

def retrieve_random_name(request):
    response = "random name chosen by dice roll"
    return HttpResponse(response)
