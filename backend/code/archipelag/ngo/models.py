from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import OneToOneField
from django.db.models import DecimalField
from django.core.validators import MinValueValidator
from decimal import Decimal


class NgoUser(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    coins = DecimalField(max_digits=100, decimal_places=1, default=10.0, validators=[MinValueValidator(Decimal('0.00'))])
    fb_token = CharField(max_length=256, blank=True)
    twitter_token = CharField(max_length=256, blank=True)

    def __str__(self):
        return str(self.user)

    def is_user_can_add_market(self, ngo):
        from archipelag.market.models import POINTS_RULES

        if ngo.coins >= POINTS_RULES['add_own_market']:
            return True
        return False

    def subtract_coins(self, ngo, number_to_subtract):
        number_to_subtract = Decimal(number_to_subtract)
        if ngo.coins >= number_to_subtract:
            ngo.coins -= number_to_subtract
            ngo.save()
            return True
        return False

    def add_coins(self, ngo, number_to_add):
        ngo.coins += Decimal(number_to_add)
        ngo.save()
