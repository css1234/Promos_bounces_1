from drf_spectacular.utils import extend_schema
from rest_framework import permissions

from core.pagination import CustomPageNumberPagination
from core.views import BaseModelViewSet

from .models import Stage, Step
from .serializers import StageSerializer, StepSerializer


@extend_schema(
    request=StepSerializer,
    responses={201: StepSerializer},
    description="Register a new user"
)

class StepViewSet(BaseModelViewSet):
    queryset = Step.objects.all().order_by('step_id')
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination


class StageViewSet(BaseModelViewSet):
    queryset = Stage.objects.select_related('step').all().order_by('stage_id')
    serializer_class = StageSerializer
    permission_classes = [permissions.IsAuthenticated]


