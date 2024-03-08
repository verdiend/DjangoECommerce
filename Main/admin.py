from django.contrib import admin
from .models import (
    Category, FoodItem, Order, OrderItem,
    # Add any additional models here
)

admin.site.register([
    Category,
    FoodItem,
    Order,
    OrderItem,
    # Add any additional models here
])