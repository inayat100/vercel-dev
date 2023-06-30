from pizza.models import pizza_type
from rest_framework import serializers

class user_api(serializers.ModelSerializer):
    class Meta:
        model = pizza_type
        fields = ['id','pizza','size','topping','price']