from django.contrib import admin
from . models import pizza_type

# Register your models here.

@admin.register(pizza_type)
class adminshow(admin.ModelAdmin):
    list_display = ['id','pizza','size','topping','price']