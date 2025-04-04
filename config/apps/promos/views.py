from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import permissions

from core.pagination import CustomPageNumberPagination
from core.views import BaseModelViewSet

from .filters import (IssuingAuthorityFilter,  # Ensure these filters exist
                      PromotionFilter, PromotionOrderFilter,
                      SanctionOrderFilter)
from .models import IssuingAuthority, Promotion, PromotionOrder, SanctionOrder
from .serializers import (IssuingAuthoritySerializer, PromotionOrderSerializer,
                          PromotionSerializer, SanctionOrderSerializer)


class IssuingAuthorityViewSet(BaseModelViewSet):
    queryset = IssuingAuthority.objects.all().order_by('issuing_authority_id')
    serializer_class = IssuingAuthoritySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = IssuingAuthorityFilter

class PromotionOrderViewSet(BaseModelViewSet):
    queryset = PromotionOrder.objects.select_related('issuing_authority', 'employee').all().order_by('-promotion_order_date')
    serializer_class = PromotionOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = PromotionOrderFilter 

class SanctionOrderViewSet(BaseModelViewSet):
    queryset = SanctionOrder.objects.select_related('issuing_authority', 'employee').all().order_by('-sanction_order_date')
    serializer_class = SanctionOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanctionOrderFilter   

class PromotionViewSet(BaseModelViewSet):
    queryset = Promotion.objects.all().order_by('-promotion_date')
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = PromotionFilter  # Apply filters


