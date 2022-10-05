from django.db import models
from account.models import Account


class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.PositiveIntegerField()
    user = models.ForeignKey(Account, related_name='user', on_delete=models.CASCADE)
