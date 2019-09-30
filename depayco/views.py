from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from django.contrib import messages

from depayco.actions import credit_cards, customers, subscriptions
from depayco.addons.decorators import already_subscribed
from depayco.addons.forms import ChargeInformationForm


@method_decorator(already_subscribed, name='dispatch')
@method_decorator(login_required, name='dispatch')
class EpaycoView(FormView):
    template_name = 'epayco-form.html'
    form_class = ChargeInformationForm


class ProcessPayment(View):
    @method_decorator(login_required)
    def post(self, request):
        try:
            token = credit_cards.tokenize(
                credit_card_number=request.POST.get('credit_card_number'),
                exp_year=request.POST.get('credit_card_exp_year'),
                exp_month=request.POST.get('credit_card_exp_month'),
                cvc=request.POST.get('cvc'),
            )['data']['id']

            customer = customers.create(
                credit_card_token=token,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                user_id=request.user.id,
                identification_type=request.POST.get('identification_type'),
                identification_number=request.POST.get('identification_number'),
            )

            subscriptions.create_and_charge(
                plan_id='pronostico_cambiario',
                customer_id=customer.id,
                credit_card_token=token,
                identification_type=request.POST.get('identification_type'),
                identification_number=request.POST.get('identification_number'),
            )
        except Exception as e:
            messages.add_message(
                request,
                messages.WARNING,
                'No se pudo procesar su pago, verifique que la información ingresada sea correcta',
            )
            form = ChargeInformationForm(request.POST)

            return render(
                request, 'epayco-form.html', {
                    'form': form
                }
            )

        return redirect(reverse('home'))


class CancelSubscription(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            subscriptions.cancel(subscription_id=request.GET.get('subscription_id'))
        except:
            messages.add_message(
                request,
                messages.WARNING,
                'No se pudo procesar su cancelación, vuelva a intentarlo más tarde.',
            )

        return redirect(reverse('my_subscription'))


class ReSubscribe(View):
    @method_decorator(already_subscribed)
    @method_decorator(login_required)
    def get(self, request):
        return render(
            request=request, template_name='re-subscribe.html'
        )

    @method_decorator(login_required)
    def post(self, request):
        try:
            subscriptions.create_and_charge(
                plan_id='pronostico_cambiario',
                customer_id=request.user.customer.id,
                credit_card_token=request.user.customer.credit_card_token,
                identification_type=request.user.customer.identification_type,
                identification_number=request.user.customer.identification_number,
            )
        except:
            messages.add_message(
                request,
                messages.WARNING,
                'No se pudo procesar su re-subscripción, vuelva a intentarlo más tarde.',
            )

        return redirect(reverse('my_subscription'))
