'''register voucher data model in django admin'''
from django.contrib import admin
from vouchers.models import Voucher


admin.site.register(Voucher)
