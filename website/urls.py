from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('createLocation', views.createLocation, name='createLocation'),

]