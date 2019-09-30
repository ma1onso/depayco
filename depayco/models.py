from django.conf import settings
from django.db import models

from depayco import epayco_client
from depayco.addons.choices import INTERVAL, IDENTIFICATION_TYPE


class Customer(models.Model):
    id = models.CharField(
        max_length=20, primary_key=True, unique=True, help_text='Example: 9xRxhaJ2YmLTkT5uz'
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    credit_card_token = models.CharField(
        max_length=20, help_text='Example: eXj5Wdqgj7xzvC7AR'
    )
    identification_type = models.CharField(
        max_length=5, choices=IDENTIFICATION_TYPE,
    )
    identification_number = models.CharField(
        max_length=200
    )
    delinquent = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.email

    def update_epayco_customer(self, update_customer_info):
        customer = epayco_client.customer.update(self.id, update_customer_info)

        return customer

    def update_epayco_credit_card(self):
        raise NotImplementedError


class Plan(models.Model):
    id = models.CharField(
        max_length=30, primary_key=True, unique=True, help_text='Example: unity_3d_course',
    )
    name = models.CharField(
        max_length=150
    )
    description = models.TextField(

    )
    amount = models.DecimalField(
        decimal_places=2, max_digits=9
    )
    currency = models.CharField(
        max_length=3,
    )
    interval = models.CharField(
        max_length=5, choices=INTERVAL,
    )
    interval_count = models.IntegerField(

    )
    trial_days = models.IntegerField(
        default=0,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    def update_epayco_plan(self, update_plan_info):
        plan = epayco_client.plan.update(self.id, update_plan_info)

        return plan


class Subscription(models.Model):
    id = models.CharField(
        max_length=20, primary_key=True, unique=True, help_text='Example: efPXtZ5r4nZRoPtjZ'
    )
    customer = models.ForeignKey(
        'depayco.Customer', on_delete=models.CASCADE,
    )
    plan = models.ForeignKey(
        'depayco.Plan', on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        default=True,
    )
    current_period_start = models.DateField(

    )
    current_period_end = models.DateField(

    )
    cancel_at_period_end = models.BooleanField(
        default=False
    )
    canceled_at = models.DateTimeField(
        null=True, blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '{0} {1}'.format(self.customer, self.plan)

    def cancel_epayco_subscription(self):
        subscription = epayco_client.subscriptions.cancel(self.id)

        return subscription
