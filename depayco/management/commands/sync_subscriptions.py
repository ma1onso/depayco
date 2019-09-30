from datetime import date

from django.core.management import BaseCommand

from depayco import epayco_client
from depayco.models import Subscription


class Command(BaseCommand):
    def handle(self, *args, **options):
        active_subscriptions = Subscription.objects.filter(is_active=True)

        for active_subscription in active_subscriptions:
            epayco_subscription = epayco_client.subscriptions.get(active_subscription.id)

            start_day, start_month, start_year = epayco_subscription['current_period_start'].split('-')
            end_day, end_month, end_year = epayco_subscription['current_period_end'].split('-')

            epayco_subscription.current_period_start = '{0}-{1}-{2}'.format(start_year, start_month, start_day)
            epayco_subscription.current_period_end = '{0}-{1}-{2}'.format(end_year, end_month, end_day)

            # TODO: verify if dates changed

            epayco_subscription.save(update_fields=['current_period_start', 'current_period_end'])

        canceled_subscriptions = Subscription.objects.filter(cancel_at_period_end=True)

        for canceled_subscription in canceled_subscriptions:
            if canceled_subscription.current_period_end <= date.today():
                canceled_subscription.is_active = True

                canceled_subscription.save(update_fields=['is_active'])
