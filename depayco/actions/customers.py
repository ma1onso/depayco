from depayco import epayco_client
from depayco.models import Customer


def create(credit_card_token, name, email, phone, user_id, identification_type, identification_number, default=True):
    """

    :param credit_card_token:
    :param name:
    :param email:
    :param phone:
    :param default:
    :param user_id:
    :param identification: {'type': 'NIT', 'number': '3434566'}
    :return:
    """
    customer_info = {
        'token_card': credit_card_token,
        'name': name,
        'email': email,
        'phone': phone,
        'default': default
    }

    customer = epayco_client.customer.create(customer_info)

    return sync_customer_from_epayco_data(
        epayco_customer_data=customer['data'],
        credit_card_token=credit_card_token,
        user_id=user_id,
        identification_type=identification_type,
        identification_number=identification_number,
    )


def update(customer_id, customer_data):
    raise NotImplementedError


def sync_customer_from_epayco_data(epayco_customer_data, credit_card_token, user_id, identification_type, identification_number):
    defaults = dict(
        user_id=user_id,
        credit_card_token=credit_card_token,
        identification_type=identification_type,
        identification_number=identification_number,
    )

    customer, created = Customer.objects.get_or_create(
        id=epayco_customer_data['customerId'],
        defaults=defaults,
    )

    return customer

