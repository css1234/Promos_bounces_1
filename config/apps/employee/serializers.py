from rest_framework import serializers

from .models import Degree, Employee


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'
        read_only_fields = ['degree_id']  # Mark primary key as read-only

class EmployeeSerializer(serializers.ModelSerializer):
    degree = DegreeSerializer(required=False)  # Make the nested degree field optional
    degree_id = serializers.PrimaryKeyRelatedField(
        queryset=Degree.objects.all(),
        source='degree',
        write_only=True,
        label="Degree ID"
    )  # For writing

    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'degree', 'degree_id', 'appointment_date']
        read_only_fields = ['employee_id']  # Mark primary key as read-only