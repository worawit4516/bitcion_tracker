from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

reverse_proxy = 'backend/'

urlpatterns = [
    path(f'{reverse_proxy}api/price_histories/', include('historical_data.urls')),
    path(f'{reverse_proxy}api/account/', include('account.urls')),
    path(f'{reverse_proxy}api/wallet/', include('wallet.urls')),
]

urlpatterns_swagger = [
    path(f'{reverse_proxy}api/', get_swagger_view(title='API Docs.', patterns=urlpatterns)),
]

urlpatterns += urlpatterns_swagger
