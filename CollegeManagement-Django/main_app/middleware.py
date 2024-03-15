from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        # Check if the user is authenticated
        if user.is_authenticated:
            # If the user is authenticated and trying to access the login page, redirect to home
            if request.path == reverse('login_page'):
                if user.user_type == '1':
                    return redirect(reverse('admin_home'))
                elif user.user_type == '2':
                    return redirect(reverse('staff_home'))
                else:
                    return redirect(reverse('student_home'))
        else:
            # If the user is not authenticated and the request path is not related to login, redirect to login
            if request.path not in [reverse('login_page'), reverse('user_login')]:
                # If it's the initial request to the home page, stay on the home page
                if request.path == reverse('home'):
                    return None
                # Otherwise, redirect to login page
                return redirect(reverse('login_page'))
