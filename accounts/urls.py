from django.urls import path
from .views import home_view, customer_view, products_view

urlpatterns = [
    path('', home_view),
    path('products/', products_view),
    path('customer/', customer_view),

]
