
import django_filters
from .models import Degree, Employee

class DegreeFilter(django_filters.FilterSet):
    degree_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search

    class Meta:
        model = Degree
        fields = ['degree_name']


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # ✅ Case-insensitive name search
    min_date = django_filters.DateFilter(field_name='appointment_date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='appointment_date', lookup_expr='lte')
    degree = django_filters.CharFilter(field_name='degree__degree_name', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['name', 'min_date', 'max_date', 'degree']  # ✅ Added name filtering
