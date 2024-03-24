from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permission_checker_admin_factory(data=None):
    def permission_checker_admin(func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_superuser:
                return func(request, *args, **kwargs)
            else:
                return redirect(reverse('login_page'))
        return wrapper
    return permission_checker_admin
