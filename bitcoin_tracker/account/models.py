from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    password = models.CharField(_('password'), max_length=128, blank=True, null=True)

    first_name = models.CharField(max_length=120, db_index=True, blank=True, null=True, default='Guest')
    last_name = models.CharField(max_length=120, db_index=True, blank=True, null=True, default='Guest')
    is_active = models.BooleanField(default=True)
    friends = models.TextField(default='[]')
    datetime_create = models.DateTimeField(auto_now_add=True)
