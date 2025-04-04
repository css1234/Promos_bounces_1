from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IssuingAuthorityViewSet, PromotionOrderViewSet,
                    PromotionViewSet, SanctionOrderViewSet)

router = DefaultRouter()
router.register(r'issuing-authorities', IssuingAuthorityViewSet)  
router.register(r'promotion-orders', PromotionOrderViewSet) 
router.register(r'sanction-orders', SanctionOrderViewSet)
router.register(r'promotions', PromotionViewSet)  # Ensure this viewset is registered

urlpatterns = [
    path('', include(router.urls)),
]