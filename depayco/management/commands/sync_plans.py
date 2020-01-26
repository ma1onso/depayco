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

                        self.stdout.write(self.style.SUCCESS(
                            f'Successfully create plan {settings_plan["id_plan"]} on epayco and local DB'
                        ))

                    elif response['success'] and not Plan.objects.filter(id=settings_plan['id_plan']).exists():
                        plans.sync_plan_from_epayco_data(epayco_plan_data=settings_plan)

                        self.stdout.write(self.style.SUCCESS(
                            f'Successfully create plan {settings_plan["id_plan"]} on local DB (from existing data on epayco)'
                        ))

                    elif response['success']:
                        plans.update(plan_id=settings_plan['id_plan'], plan_data=settings_plan)

                        self.stdout.write(self.style.SUCCESS(
                            f'Successfully update plan {settings_plan["id_plan"]} on epayco and local DB'
                        ))

        except AttributeError:
            self.stdout.write(self.style.WARNING('Is needed configure PLANS in settings.py'))
