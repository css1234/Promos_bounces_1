from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Role
from .serializers import (AssignRoleSerializer,
                          CustomTokenObtainPairSerializer, RoleSerializer,
                          UserListSerializer, UserRegistrationSerializer)


@extend_schema(
    request=UserRegistrationSerializer,
    responses={201: UserRegistrationSerializer},
    description="Register a new user"
)
class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # Don't Allow anyone to register

    def post(self, request, *args, **kwargs):
        """Handle user registration"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    responses={200: UserListSerializer(many=True)},
    description="Get a list of all users"
)
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RoleViewSet(ModelViewSet):
    """
    A viewset for CRUD operations on the Role model.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Check if the logged-in user has the 'Admin' role
        if not self.request.user.profile.role or self.request.user.profile.role.name != 'Admin':
            raise PermissionDenied("You do not have permission to access this resource.")
        return super().get_queryset()

class AssignRoleView(APIView):
    """
    API view to assign a role to a user.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=AssignRoleSerializer,  # Specify the serializer for the request body
        responses={200: {"message": "Role assigned successfully."}},  # Define the response schema
        description="Assign a role to a user by providing user_id and role_id."
    )
    def post(self, request, *args, **kwargs):
        serializer = AssignRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Role assigned successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
