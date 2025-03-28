# filepath: d:\Promos_bounces_1\config\apps\users\url.py
from django.urls import path
from .views import UserRegistrationView, UserListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('list/', UserListView.as_view(), name='user-list'),  # New URL pattern for listing users
]