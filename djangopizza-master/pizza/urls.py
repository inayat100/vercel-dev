from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>/',views.update_pizza,name='update'),
    path('delet/<int:id>/',views.delet_pizza,name='delet'),
    path('singup/',views.user_singup,name='singup'),
    path('singin/',views.user_singin,name='singin'),
    path('logout/',views.user_logout,name='logout'),
    path('user/',views.user_chek,name='user'),
    path('api/',include('pizza.api.urls'))

]