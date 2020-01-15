''' Data Model module'''
from django.db import models
from django.core import validators


DISCOUNT_CHOICES = [
        ('RM', 'RM'),
        ('%', '%'),
        ]

class Voucher(models.Model):
    '''Class for representing the Voucher data model'''
    code = models.CharField(max_length=32, unique=True)
    use_count = models.IntegerField(validators=[
                validators.MinValueValidator(0),
                validators.MaxValueValidator(3)],
                                    default=0)
    active = models.BooleanField(default=True)
    discount_value = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    discount = models.CharField(max_length=32,
                                choices=DISCOUNT_CHOICES,
                                default='RM 10 off')

    def __str__(self):
        ''' string representation of Voucher data model '''
        return self.code
