from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product, Order
# Create your views here.

def home_view(request):
    customers = Customer.objects.all()
    last_five_orders = Order.objects.all()
    total_orders= Order.objects.all().count()
    delivered_orderd_count = Order.objects.filter(status = 'Delivered').count()
    pending_orderd_count = Order.objects.filter(status = 'Pending').count()
    
    context = {
        'customers' : customers,
        'last_five_orders' : last_five_orders,
        'total_orders':total_orders,
        'delivered_orderd_count' : delivered_orderd_count,
        'pending_orderd_count' : pending_orderd_count
    }
    return render(request, 'accounts/dashboard.html', context = context)

def customer_view(request):
    
    return HttpResponse('Customer')

def products_view(request):
    return HttpResponse('products')