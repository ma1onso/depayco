## Introduction
Django integration with epayco.co

## CONFIGURATIONS (settings.py)

**EPAYCO_PUBLIC_KEY**: String

**EPAYCO_SECRET_KEY**: String

**DEBUG_EPAYCO**: Boolean

**PLANS**
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
TODOs:
- [ ] Upload to pypi
- [ ] Support User model out the auth.models.User
