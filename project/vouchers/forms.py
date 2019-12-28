'''forms for input'''
from django import forms


class VoucherInputForm(forms.Form):
    '''create voucher code input form fields '''
    code = forms.CharField(label='Voucher Code')
