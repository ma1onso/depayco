from django.conf.urls import url

from .views import EpaycoView, ProcessPayment, CancelSubscription, ReSubscribe

urlpatterns = [
    url(r'^epayco-form/$', EpaycoView.as_view(), name='epayco_form'),
    url(r'^process-payment/$', ProcessPayment.as_view(), name='process_payment'),
    url(r'^cancel-subscription/$', CancelSubscription.as_view(), name='cancel_subscription'),
    url(r'^re-subscribe/$', ReSubscribe.as_view(), name='re_subscribe'),
]
