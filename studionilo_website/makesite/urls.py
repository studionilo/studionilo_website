from django.urls import path
from . import views as makesite_views

urlpatterns = [
    path('', makesite_views.home, name='makesite_home'),
]