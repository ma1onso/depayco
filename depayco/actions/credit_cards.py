from depayco import epayco_client


def tokenize(credit_card_number, exp_year, exp_month, cvc):
    if len(exp_month) == 1:
        exp_month = '0{exp_month}'.format(exp_month=exp_month)

    credit_card_data = {
        'card[number]': credit_card_number.replace(' ', ''),
        'card[exp_year]': exp_year.replace(' ', ''),
        'card[exp_month]': exp_month.replace(' ', ''),
        'card[cvc]': cvc.replace(' ', ''),
    }

    return epayco_client.token.create(credit_card_data)
