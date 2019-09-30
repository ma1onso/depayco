from django.conf import settings
from pyepayco import epayco

options = {
    'apiKey': settings.EPAYCO_PUBLIC_KEY,
    'privateKey': settings.EPAYCO_SECRET_KEY,
    'test': settings.DEBUG_EPAYCO,
    'lenguage': 'EN',
}

epayco_client = epayco.Epayco(options)
