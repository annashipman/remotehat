from django.urls import path

from . import views

app_name = 'hat'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit_name', views.submit_name, name='submit_name'),
    path('retrieve_name', views.retrieve_random_name, name='retrieve_random_name'),
]
