from django.contrib import admin

from .models import Customer, Plan, Subscription

admin.site.register(Customer)
admin.site.register(Plan)
admin.site.register(Subscription)
