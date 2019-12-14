from django import forms

class VoucherInputForm(forms.Form):
    code =forms.CharField(label='Voucher Code')
