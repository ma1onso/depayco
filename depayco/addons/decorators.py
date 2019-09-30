from django.shortcuts import redirect
from django.urls import reverse


def subscription_required(function):
    """
    """
    def return_function(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)

        if hasattr(request.user, 'customer'):
            if not request.user.customer.subscription_set.filter(is_active=True).exists():
                return redirect(reverse('depayco:re_subscribe'))
            else:
                return function(request, *args, **kwargs)

        elif request.user.is_authenticated():
            return redirect(reverse('depayco:epayco_form'))
        else:
            return redirect('sign_up')

    return return_function


def already_subscribed(function):
    """
    """
    def return_function(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)

        if hasattr(request.user, 'customer'):
            if request.user.customer.subscription_set.filter(is_active=True).exists():
                return redirect(reverse('home'))
            else:
                return function(request, *args, **kwargs)

        elif request.user.is_authenticated():
            return function(request, *args, **kwargs)
        else:
            return redirect('sign_up')

    return return_function
