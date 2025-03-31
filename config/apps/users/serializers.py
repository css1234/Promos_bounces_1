from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Role, Profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password], 
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True, required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        """Ensure passwords match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "The two password fields must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 before saving
        validated_data['username'] = validated_data['username'].lower()  # Normalize username
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔹 Add custom claims inside the token
        token['user_id'] = user.id
        token['username'] = user.username
        token['first_name'] = user.first_name  
        token['last_name'] = user.last_name
        if user.profile and user.profile.role:
            token['role'] = user.profile.role.name

        return token        

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class AssignRoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    role_id = serializers.IntegerField(required=True)

    def validate(self, data):
        # Validate the user exists
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            raise serializers.ValidationError({"user_id": "User not found."})

        # Validate the role exists
        try:
            role = Role.objects.get(id=data['role_id'])
        except Role.DoesNotExist:
            raise serializers.ValidationError({"role_id": "Role not found."})

        data['user'] = user
        data['role'] = role
        return data

    def save(self):
        user = self.validated_data['user']
        role = self.validated_data['role']

        # Assign the role to the user's profile
        profile, created = Profile.objects.get_or_create(user=user)
        profile.role = role
        profile.save()
        return profile