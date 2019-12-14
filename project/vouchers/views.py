from django.shortcuts import render
from vouchers.models import Voucher
from vouchers.forms import VoucherInputForm

def submit_code(request):
    form = VoucherInputForm()
    if request.method == "POST":
        form =VoucherInputForm(request.POST)
        if form.is_valid():
            try:
                code= form.cleaned_data['code']
                voucher = Voucher.objects.get(code=code, active=True)
                update_voucher(voucher)
                return render(request, "vouchers/voucherInput.html", {'form': form, 'discount': voucher.discount}) 
            except Voucher.DoesNotExist:
                return render(request, "vouchers/voucherInput.html", {'form': form,
                                                                     'error_message': return_error_message()})
    return render(request, "vouchers/voucherInput.html", {'form': form})
      
def return_error_message():
    return 'Invalid Code! Your code i either wrong or already expired.'
    

def update_voucher(voucher):
    voucher.use_count += 1
    voucher.save()
    

