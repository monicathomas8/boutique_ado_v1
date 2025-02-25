from django.contrib import admin
from django.urls import path
from . import views


# URL patterns for the home app

urlpatterns = [
    # Home page view
    path('', views.index, name='home'),
]
