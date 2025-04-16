from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Product, Order
from .forms import OrderForm
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

def customer_view(request, customer_pk):
    customer = Customer.objects.get(id=customer_pk)
    orders = customer.order_set.all()
    context = {
    'customer' : customer,
    'orders' : orders
    }
    
    return render(request=request, template_name='accounts/customer.html', context=context)

def products_view(request):
    return HttpResponse('products')


def create_order_view(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid:
            order_form.save()
            return redirect('home')
            
    context = {
        'order_form' : order_form
    }
    return render(request=request, template_name='accounts/order_form.html', context=context)

def update_order_view(request, order_pk):
    order = Order.objects.get(id=order_pk)
    order_form = OrderForm(instance=order)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid:
            order_form.save()
            return redirect('home')
    context = {
        'order_form' : order_form
    }
    return render(request=request, template_name='accounts/order_form.html', context=context)

def delete_order_view(request, order_pk):
    context = {
        'item' : order
    }
    return render(request=request, template_name='accounts/delete.html', context=context)