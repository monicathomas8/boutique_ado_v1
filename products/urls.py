from django.urls import path
from . import views


# URL patterns for the home app

urlpatterns = [
    # Home page view
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
