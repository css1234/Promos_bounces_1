from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DegreeViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'degrees', DegreeViewSet)  # /api/degrees/
router.register(r'employees', EmployeeViewSet)  # /api/employees/

urlpatterns = [
    path('', include(router.urls)),
]
