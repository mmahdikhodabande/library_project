from django.urls import path
from . import views

urlpatterns = [
    path('add-to-order', views.add_to_order, name='add_to_order_page'),
    path('user-basket', views.user_basket, name='user_basket_page')
]
