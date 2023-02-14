from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('testing/', views.testing, name='testing'),
    path('modeltesting/', views.modeltesting, name='modeltesting'),
    path('home/', views.homepage, name='homepage'),
    path('NHL/', views.nhl, name='nhl'),
    path('NFL/', views.nfl, name='nfl'),
    path('NBA/', views.nba, name='nba'),
    path('MLB/', views.mlb, name='mlb'),
    path('Golf/', views.golf, name='golf'),
]