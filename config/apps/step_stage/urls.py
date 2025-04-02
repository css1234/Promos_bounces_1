from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StepViewSet, StageViewSet

router = DefaultRouter()
router.register(r'steps', StepViewSet)
router.register(r'stages', StageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]