from django.contrib import admin
from django.urls import path, include

reverse_proxy = 'backend/'

urlpatterns = [
    path(f'{reverse_proxy}api/price_histories/', include('historical_data.urls')),
    path(f'{reverse_proxy}api/account/', include('account.urls')),
    path(f'{reverse_proxy}api/wallet/', include('wallet.urls')),
]
