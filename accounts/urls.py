from django.urls import path
from .views import home_view, customer_view, products_view, create_order_view, update_order_view,delete_order_view, signup_view,login_view, logout_view, user_view

urlpatterns = [
    path('', home_view, name= 'home'),
    path('products/', products_view, name='products'),
    path('customer/<str:customer_pk>/', customer_view, name= 'customer'),
    path('create_order/<str:customer_pk>', create_order_view, name= 'create_order'),
    path('update_order/<str:order_pk>/', update_order_view, name= 'update_order'),
    path('delete_order/<str:order_pk>', delete_order_view, name= 'delete_order'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view,name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', user_view, name='user')

]
