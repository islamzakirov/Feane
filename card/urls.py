from django.urls import path, include
from .views import *

urlpatterns = [
   path('', card, name="card"),
   path('add_product/<int:product_id>/', add_cart, name="cart_add"),
   path('sub_product/<int:product_id>/', sub_cart, name="cart_sub"),
   path('remove_product/<int:product_id>/', remove_cart_item, name="cart_remove")
]

