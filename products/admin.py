from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
# This code imports the Product and Category models from the models module and registers them with the admin site.
# This will make the Product and Category models accessible via the Django admin interface.

