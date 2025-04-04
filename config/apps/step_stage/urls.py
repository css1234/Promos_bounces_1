from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StageViewSet, StepViewSet

router = DefaultRouter()
router.register(r'steps', StepViewSet)
router.register(r'stages', StageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]