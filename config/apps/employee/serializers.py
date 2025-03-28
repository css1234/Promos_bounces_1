from rest_framework import serializers
from .models import Degree, Employee

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    degree = DegreeSerializer(read_only=True)  # Nested representation of Degree
    degree_id = serializers.PrimaryKeyRelatedField(queryset=Degree.objects.all(), source='degree', write_only=True)  # For writing

    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'degree', 'degree_id', 'appointment_date']