from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Account


class Wallet(models.Model):
    wallet_id = models.CharField(_('wallet'), max_length=50, primary_key=True)
    user = models.ForeignKey(Account, related_name='user_wallet', on_delete=models.CASCADE)
    link_account = models.TextField(default='[]')

    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    volume = models.PositiveIntegerField(blank=True, null=True, default=0)
    is_active = models.BooleanField(default=True)
    datetime_create = models.DateTimeField(auto_now_add=True)
