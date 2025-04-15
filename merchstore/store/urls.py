from django.urls import path
from .views import *

urlpatterns = [
    #INDEX LANDING PAGE
    path('', product_list, name="product_list"), 
    
    path('items/',product_list, name="product_list" ),
    path('item/<int:num>/', product_detail, name="product_detail"),
    path('item/add/', product_create, name="product_create"),
    path('item/<int:num>/edit/', product_update, name="product_update"),
    path('cart/',cart, name="cart"),
    path('transactions/', transactions, name="transactions")
    
]

app_name = "store"