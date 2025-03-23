from django.urls import path
from . import views


# URL patterns for the home app

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
]
