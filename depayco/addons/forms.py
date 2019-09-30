from django import forms

from depayco.addons.choices import IDENTIFICATION_TYPE


class ChargeInformationForm(forms.Form):
    name = forms.CharField(
        max_length=50,
    )
    email = forms.EmailField(

    )
    credit_card_number = forms.CharField(
        max_length=50
    )
    cvc = forms.CharField(
        max_length=4,
    )
    credit_card_exp_month = forms.CharField(
        max_length=2,
    )
    credit_card_exp_year = forms.CharField(
        max_length=4,
    )
    phone = forms.CharField(
        max_length=10,
    )
    identification_type = forms.ChoiceField(
        choices=IDENTIFICATION_TYPE,
    )
    identification_number = forms.CharField(
        max_length=200,
    )
