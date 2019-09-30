from datetime import datetime

from depayco import epayco_client
from depayco.models import Subscription


def create_and_charge(plan_id, customer_id, credit_card_token, identification_type, identification_number):
    subscription_data = {
        'id_plan': plan_id,
        'customer': customer_id,
        'token_card': credit_card_token,
        'doc_type': identification_type,
        'doc_number': identification_number,
    }

    epayco_subscription = epayco_client.subscriptions.create(subscription_data)
    epayco_subscription_charge = epayco_client.subscriptions.charge(subscription_data)

    return sync_subscription_from_epayco_data(
        epayco_subscription_data=epayco_subscription,
        epayco_subscription_data_charge=epayco_subscription_charge,
        customer_id=customer_id,
        plan_id=plan_id,
    )


def cancel(subscription_id):
    epayco_client.subscriptions.cancel(subscription_id)

    return sync_cancel_subscription(subscription_id=subscription_id)


def has_active_subscription(subscription_id):
    raise NotImplementedError


def intervals_paid(customer_id):
    raise NotImplementedError


def sync_subscription_from_epayco_data(epayco_subscription_data, epayco_subscription_data_charge, customer_id, plan_id):
    start_day, start_month, start_year = epayco_subscription_data['current_period_start'].split('-')
    end_day, end_month, end_year = epayco_subscription_data_charge['subscription']['periodEnd'].split('-')

    defaults = dict(
        customer_id=customer_id,
        plan_id=plan_id,
        current_period_start='{0}-{1}-{2}'.format(start_year, start_month, start_day),
        current_period_end='{0}-{1}-{2}'.format(end_year, end_month, end_day),
    )

    subscription, created = Subscription.objects.get_or_create(
        id=epayco_subscription_data['id'],
        defaults=defaults,
    )

    if created is False:
        subscription.cancel_at_period_end = False
        subscription.save(update_fields=['cancel_at_period_end'])

    return subscription


def sync_cancel_subscription(subscription_id):
    return Subscription.objects.filter(id=subscription_id).update(
        cancel_at_period_end=True, canceled_at=datetime.today()
    )
