from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserListSerializer
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema

@extend_schema(
    request=UserRegistrationSerializer,
    responses={201: UserRegistrationSerializer},
    description="Register a new user"
)
class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Allow anyone to register

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
