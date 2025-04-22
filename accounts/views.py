from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Customer, Product, Order
from .forms import OrderForm, CustomUserCreationForm
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decoratores import unauthenticated_user, admin_only, allowed_users
from django.contrib.auth.models import Group
# Create your views here.

@unauthenticated_user
def signup_view(request):
    signup_form = CustomUserCreationForm()
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            Customer.objects.create(user = user, name = 'unnamed')
            username = signup_form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created!')
            return redirect('login')
    context = {
        'signup_form' : signup_form
    }
    return render(request=request, template_name='accounts/signup.html', context=context)

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            next = request.GET.get('next')
            print(next)
            if next:
                return redirect(next)
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect!')
    return render(request=request, template_name='accounts/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
@admin_only
def customer_view(request, customer_pk):
    customer = Customer.objects.get(id=customer_pk)
    orders = customer.order_set.all()
    order_filter = OrderFilter(request.GET, queryset = orders)
    orders = order_filter.qs
    context = {
    'customer' : customer,
    'orders' : orders,
    'order_filter' : order_filter
    }
    
    return render(request=request, template_name='accounts/customer.html', context=context)

@login_required(login_url='login')
@admin_only
def products_view(request):
    return HttpResponse('products')

@admin_only
def create_order_view(request, customer_pk):
    customer = Customer.objects.get(id = customer_pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'),extra=5, can_delete=False)
    order_formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST, instance=customer)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home')
        else:
            print(order_formset.errors)
            
    context = {
        'order_formset' : order_formset
    }
    return render(request=request, template_name='accounts/order_form.html', context=context)

@admin_only
def update_order_view(request, order_pk):
    order = Order.objects.get(id=order_pk)
    order_form = OrderForm(instance=order)
    if request.method == 'POST':
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('home')
    context = {
        'order_form' : order_form
    }
    return render(request=request, template_name='accounts/order_form.html', context=context)

@login_required(login_url='login')
@admin_only
def delete_order_view(request, order_pk):
    order = Order.objects.get(id = order_pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {
        'item' : order
    }
    return render(request=request, template_name='accounts/delete.html', context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_view(request):
    user = request.user
    customer = user.customer
    orders = customer.order_set.all()
    order_filter = OrderFilter(request.GET, queryset = orders)
    orders = order_filter.qs
    context = {
    'customer' : customer,
    'orders' : orders,
    'order_filter' : order_filter
    }
    return render(request=request, template_name='accounts/user.html', context=context)