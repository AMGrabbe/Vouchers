from django.db import models
from django.core import validators
from django.db.models.signals import post_save


DISCOUNT_CHOICES=[
            ('RM 10 off','RM 10 off'),
            ('10% off', '10% off'),
]

class Voucher(models.Model):
    code = models.CharField(max_length=32, unique = True)
    use_count = models.IntegerField(validators = [validators.MinValueValidator(0),validators.MaxValueValidator(3)], default = 0)
    active = models.BooleanField(default = True)
    discount = models.CharField(max_length = 32, choices = DISCOUNT_CHOICES, default = 'RM 10 off')

    def __str__(self):
        return self.code




def checkValidity(sender, instance, **kwargs):
    if instance.use_count>=3:
        instance.active = False
    post_save.disconnect(checkValidity, sender=Voucher)
    instance.save()
    post_save.connect(checkValidity, sender=Voucher)


post_save.connect(checkValidity, sender=Voucher)
