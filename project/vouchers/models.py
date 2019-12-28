''' Data Model module'''
from django.db import models
from django.core import validators
from django.db.models.signals import post_save


DISCOUNT_CHOICES = [
        ('RM 10 off', 'RM 10 off'),
        ('10% off', '10% off'),
        ]


# put check_validity into forms
def check_validity(instance):
    '''checks voucher user inputs activity status '''
    if instance.use_count >= 3:
        instance.active = False
    post_save.disconnect(check_validity, sender=Voucher)
    instance.save()
    post_save.connect(check_validity, sender=Voucher)


post_save.connect(check_validity, sender=Voucher)


class Voucher(models.Model):
    '''Class for representing the Voucher data model'''
    code = models.CharField(max_length=32, unique=True)
    use_count = models.IntegerField(validators=[
                validators.MinValueValidator(0),
                validators.MaxValueValidator(3)],
                                    default=0)
    active = models.BooleanField(default=True)
    discount = models.CharField(max_length=32,
                                choices=DISCOUNT_CHOICES,
                                default='RM 10 off')

    def __str__(self):
        ''' string representation of Voucher data model '''
        return self.code
