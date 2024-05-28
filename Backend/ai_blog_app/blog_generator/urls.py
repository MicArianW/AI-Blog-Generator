from django.urls import path
from .import views #when ever user tries to go to the homepage, its going to go the views file

urlpatterns = [
    # takes list of urls
    path('', views.index, name='index') #trying to create url for the homepage
    
]