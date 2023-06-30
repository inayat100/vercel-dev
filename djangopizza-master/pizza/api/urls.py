from django.urls import path,include
from pizza.api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('pizza',views.user_view,basename='pizza')

urlpatterns = [
    path('',include(router.urls))
]