# filepath: d:\Promos_bounces_1\config\apps\users\url.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AssignRoleView, CustomTokenObtainPairView, RoleViewSet,
                    UserListView, UserRegistrationView)

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='user-list'),  # New URL pattern for listing users
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('assign-role/', AssignRoleView.as_view(), name='assign-role'),  # Add URL for assigning roles
    path('', include(router.urls)),  # Include router URLs
]