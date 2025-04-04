# my_app/views.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.pagination import \
    PageNumberPagination  # Replace with default pagination if needed
from rest_framework.response import Response

from core.pagination import \
    CustomPageNumberPagination  # Ensure this pagination class exists
from core.views import BaseModelViewSet  # Ensure this base viewset exists

from .filters import DegreeFilter, EmployeeFilter  # Ensure these filters exist
from .models import Degree, Employee
from .serializers import DegreeSerializer, EmployeeSerializer


class DegreeViewSet(BaseModelViewSet):
    queryset = Degree.objects.all().order_by('degree_id')
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = DegreeFilter  # Apply filters


class EmployeeViewSet(BaseModelViewSet):
    queryset = Employee.objects.select_related('degree').all().order_by('-appointment_date')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Use custom pagination if available
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter  # Apply filters
