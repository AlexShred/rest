from django.contrib import admin

from .models import User, Client, Worker, Ingredient, Food, Order

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Order)