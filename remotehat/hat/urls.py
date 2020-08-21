from django.urls import path

from . import views

app_name = 'hat'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_name', views.add_name, name='add_name'),
    path('play', views.play, name='play'),
    path('retrieve_name', views.retrieve_random_name, name='retrieve_random_name'),
    path('submit_name', views.submit_name, name='submit_name'),
]
