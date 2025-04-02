
import django_filters
from .models import IssuingAuthority , PromotionOrder , SanctionOrder , Promotion

class IssuingAuthorityFilter(django_filters.FilterSet):
    issuing_authority_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search

    class Meta:
        model = IssuingAuthority
        fields = ['issuing_authority_name']


class PromotionOrderFilter(django_filters.FilterSet):
    promotion_order_no = django_filters.CharFilter(field_name='promotion_order_no', lookup_expr='icontains')  # ✅ Case-insensitive name search
    min_date = django_filters.DateFilter(field_name='promotion_order_date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='promotion_order_date', lookup_expr='lte')
    # degree = django_filters.CharFilter(field_name='degree__degree_name', lookup_expr='icontains')

    class Meta:
        model = PromotionOrder
        fields = ['promotion_order_no', 'min_date', 'max_date']  # ✅ Added name filtering

class SanctionOrderFilter(django_filters.FilterSet):
    sanction_order_no = django_filters.CharFilter(field_name='sanction_order_no', lookup_expr='icontains')  # ✅ Case-insensitive name search
    min_date = django_filters.DateFilter(field_name='sanction_order_date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='sanction_order_date', lookup_expr='lte')
    # degree = django_filters.CharFilter(field_name='degree__degree_name', lookup_expr='icontains')

    class Meta:
        model = SanctionOrder
        fields = ['sanction_order_no', 'min_date', 'max_date']  # ✅ Added name filtering

class PromotionFilter(django_filters.FilterSet):
    # promotion_order_no = django_filters.CharFilter(field_name='promotion_order_no', lookup_expr='icontains')  # ✅ Case-insensitive name search
    min_date = django_filters.DateFilter(field_name='promotion_date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='promotion_date', lookup_expr='lte')
    employee = django_filters.CharFilter(field_name='employee__name', lookup_expr='icontains')

    class Meta:
        model = Promotion
        fields = ['min_date', 'max_date']  # ✅ Added name filtering
