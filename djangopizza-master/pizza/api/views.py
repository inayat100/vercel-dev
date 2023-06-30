from pizza.models import pizza_type
from pizza.api.serializers import user_api
from rest_framework import viewsets


class user_view(viewsets.ModelViewSet):
    queryset = pizza_type.objects.all()
    serializer_class = user_api