from rest_framework import serializers
from apps.employee.models import Employee
from apps.promos.models import IssuingAuthority, PromotionOrder, SanctionOrder, Promotion
from apps.employee.serializers import EmployeeSerializer


class IssuingAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuingAuthority
        fields = '__all__'
        read_only_fields = ['issuing_authority_id']


class PromotionOrderSerializer(serializers.ModelSerializer):
    issuing_authority = IssuingAuthoritySerializer(read_only=True)
    issuing_authority_id = serializers.PrimaryKeyRelatedField(
        queryset=IssuingAuthority.objects.all(), 
        source='issuing_authority', 
        write_only=True,
        label="Issuing Authority ID")
    
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), 
        source='employee', 
        write_only=True,
        label="Employee ID")

    class Meta:
        model = PromotionOrder
        fields = ['promotion_order_id', 'promotion_order_no', 'promotion_order_date', 'issuing_authority', 'issuing_authority_id', 'employee', 'employee_id', 'promotion_value']
        read_only_fields = ['promotion_order_id']

class SanctionOrderSerializer(serializers.ModelSerializer):
    issuing_authority = IssuingAuthoritySerializer(read_only=True)
    issuing_authority_id = serializers.PrimaryKeyRelatedField(queryset=IssuingAuthority.objects.all(), source='issuing_authority', write_only=True)
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)

    class Meta:
        model = SanctionOrder
        fields = ['sanction_order_id', 'sanction_order_no', 'sanction_order_date', 'issuing_authority', 'issuing_authority_id', 'employee', 'employee_id', 'sanction_value']
        read_only_fields = ['sanction_order_id']

class PromotionSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), 
        source='employee', 
        write_only=True,
        label="Employee ID"
    )

    class Meta:
        model = Promotion
        fields = ['promotion_id', 'employee', 'employee_id', 'promotion_date']
        read_only_fields = ['promotion_id']