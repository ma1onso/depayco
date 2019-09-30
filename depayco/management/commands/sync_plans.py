from django.conf import settings
from django.core.management import BaseCommand

from depayco import epayco_client
from depayco.actions import plans
from depayco.models import Plan


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            if len(settings.PLANS) > 0:
                for settings_plan in settings.PLANS:
                    response = epayco_client.plan.get(settings_plan['id_plan'])

                    if 'message' in response and response['message'] == 'Plan no encontrado':
                        plans.create(plan_data=settings_plan)
                    elif response['success'] and not Plan.objects.filter(id=settings_plan['id_plan']).exists():
                        plans.sync_plan_from_epayco_data(epayco_plan_data=settings_plan)
                    elif response['success']:
                        plans.update(plan_id=settings_plan['id_plan'], plan_data=settings_plan)

                    self.stdout.write(self.style.SUCCESS(
                        'Successfully create or update plan "%s" on epayco and local DB' %
                        settings_plan['id_plan']
                    ))

        except AttributeError:
            self.stdout.write(self.style.WARNING('Is needed configure PLANS in settings.py'))
