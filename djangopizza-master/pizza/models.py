from django.db import models

# Create your models here.

class pizza_type(models.Model):
    type_of_pizza = (
        ('Regular','Regular'),
        ('Square','Square'),
        ('Marol','Marol'),
        ('Farmhouse','Farmhouse'),
    )

    size_of_pizza = (
        ('10 inche','10 inche'),
        ('12 inche','12 inche'),
        ('14 inche','14 inche'),
        ('16 inche','16 inche'),
        ('18 inche','18 inche'),
    )
    topping_of_pizza = (
        ('potato','potato'),
        ('broccoli','broccoli'),
        ('eggplant','eggplant'),
        ('mushroom','mushroom'),
        ('black olives','black olives'),
        ('fresh garlic','fresh garlic'),
        ('onion','onion'),
        ('tomato','tomato'),
    )
    pizza = models.CharField(max_length=50, choices = type_of_pizza)
    size = models.CharField(max_length=50, choices = size_of_pizza)
    topping = models.CharField(max_length=50, choices = topping_of_pizza)
    price = models.CharField(max_length=50)










