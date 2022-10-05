from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from historical_data.views import PriceHistoryView

router = DefaultRouter()
router.register(r'', PriceHistoryView)
# router.register(r'{pk}$', PriceHistoryView, 'retrieve-price_history-detail'),
# router.register(r'/{pk}/$', PriceHistoryView, 'retrieve-price_history-detail'),
urlpatterns = router.urls
