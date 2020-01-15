'''forms for input'''
from django import forms
from django.core.exceptions import ValidationError
from vouchers.models import Voucher


class VoucherInputForm(forms.Form):
   # code = forms.CharField(label='Voucher Code')
    '''connect model to field'''
    code = forms.CharField(label='Voucher Code')

    def clean(self):
        '''Check if input code is active'''
        super().clean()
        code = self.cleaned_data['code']
        if Voucher.objects.filter(code__exact=code) and not Voucher.objects.filter(active=True):
            raise ValidationError("Not Active")

        if not Voucher.objects.filter(code__exact=code):
            raise ValidationError("Not Existing")
        