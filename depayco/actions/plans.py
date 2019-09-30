from depayco import epayco_client
from depayco.models import Plan


def create(plan_data):
    epayco_plan = epayco_client.plan.create(plan_data)

    return sync_plan_from_epayco_data(epayco_plan['data'])


def delete(plan_id):
    epayco_client.plan.delete(plan_id)

    return Plan.objects.get(id=plan_id).delete()


def update(plan_id, plan_data):
    copy_plan_data = remove_plan_key(plan_data=plan_data)
    epayco_client.plan.update(plan_id, copy_plan_data)

    return update_plan(plan_data=plan_data)


def sync_plan_from_epayco_data(epayco_plan_data):
    defaults = dict(
        name=epayco_plan_data['name'],
        description=epayco_plan_data['description'],
        amount=epayco_plan_data['amount'],
        currency=epayco_plan_data['currency'],
        interval=epayco_plan_data['interval'],
        interval_count=epayco_plan_data['interval_count'],
        trial_days=epayco_plan_data['trial_days'],
    )

    plan, created = Plan.objects.get_or_create(
        id=epayco_plan_data['id_plan'],
        defaults=defaults,
    )

    return plan


def update_plan(plan_data):
    plan = Plan.objects.get(id=plan_data['id_plan'])

    plan.name = plan_data['name']
    plan.description = plan_data['description']
    plan.amount = plan_data['amount']
    plan.currency = plan_data['currency']
    plan.interval = plan_data['interval']
    plan.interval_count = plan_data['interval_count']
    plan.trial_days = plan_data['trial_days']

    plan.save()


def remove_plan_key(plan_data, key='id_plan'):
    copy_plan_data = dict(plan_data)
    del copy_plan_data[key]

    return copy_plan_data
