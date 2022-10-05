from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from account.views import AccountView

router = DefaultRouter()
router.register(r'', AccountView)
urlpatterns = router.urls
