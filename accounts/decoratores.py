from django.shortcuts import redirect
from django.http import HttpResponse
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        user_groups = []
        if(request.user.groups.exists()):
            user_groups = map(lambda group:group.name,request.user.groups.all())
        if('admin' in user_groups):
            return view_func(request, *args, **kwargs)
        if('customer' in user_groups):
            return redirect('user')
        return HttpResponse('You do not have the permession to access this page')
    return wrapper_func

def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user_groups = []
            if(request.user.groups.exists()):
                user_groups = map(lambda group:group.name,request.user.groups.all())
            if(any(group in allowed_roles for group in user_groups)):
                return view_func(request, *args, **kwargs)
            return HttpResponse('You do not have the permession to access this page')
        return wrapper_func
    return decorator 