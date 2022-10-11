from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from wallet.views import WalletView

router = DefaultRouter()
router.register(r'', WalletView)
urlpatterns = router.urls
