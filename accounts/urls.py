from django.urls import path
from .views import home_view, customer_view, products_view, create_order_view, update_order_view,delete_order_view

urlpatterns = [
    path('', home_view, name= 'home'),
    path('products/', products_view, name='products'),
    path('customer/<str:customer_pk>/', customer_view, name= 'customer'),
    path('create_order/', create_order_view, name= 'create_order'),
    path('update_order/<str:order_pk>/', update_order_view, name= 'update_order'),
    path('delete_order/<str:order_pk>', delete_order_view, name= 'delete_order')

]
