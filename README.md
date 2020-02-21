Django integration with ePayco ([epayco.co](https://www.epayco.co)), Colombian payment gateway.

## Installation
- `pip install depayco`

- Set _depayco_ on INSTALLED_APPS

- Set secret and public key in `settings`:

    **EPAYCO_PUBLIC_KEY**: String

    **EPAYCO_SECRET_KEY**: String
    
- Add plans to `settings` file:

    ```
    PLANS = (
        {
            'id_plan': 'love2d_course',
            'name': 'love2d Course',
            'description': 'The most beautiful love2d course',
            'amount': 29.99,
            'currency': 'USD',
            'interval': 'month',
            'interval_count': 1,
            'trial_days': 14,
        },
        {
            'id_plan': 'defold_course',
            'name': 'defold Course',
            'description': 'The most mad defold course',
            'amount': 29.99,
            'currency': 'USD',
            'interval': 'month',
            'interval_count': 1,
            'trial_days': 14,
        }
    )
    ```
**Note**: for create plan in epayco.co run command `sync_plans`

- Create tables in DB `python manage.py migrate`

## Commands

`python manage.py sync_plans` to create plans on epayco.co

`python manage.py sync_subscriptions` to keep update your subscriptions on DB

## Configurations

**DEBUG_EPAYCO**: Boolean

**EPAYCO_PUBLIC_KEY**: String

**EPAYCO_SECRET_KEY**: String

**PLANS**: Tuple of dictionaries

## Buy me a coffee

[![](https://cdn4.iconfinder.com/data/icons/simple-peyment-methods/512/paypal-64.png)](https://paypal.me/alonsoenrique)
