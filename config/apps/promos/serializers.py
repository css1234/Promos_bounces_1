from rest_framework import serializers
from config.apps.employee.models import Employee
from config.apps.promos.models import IssuingAuthority, PromotionOrder, SanctionOrder, Promotion
from config.apps.employee.serializers import EmployeeSerializer


class IssuingAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuingAuthority
        fields = '__all__'

class PromotionOrderSerializer(serializers.ModelSerializer):
    issuing_authority = IssuingAuthoritySerializer(read_only=True)
    issuing_authority_id = serializers.PrimaryKeyRelatedField(queryset=IssuingAuthority.objects.all(), source='issuing_authority', write_only=True)
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)

    class Meta:
        model = PromotionOrder
        fields = ['promotion_order_id', 'promotion_order_no', 'promotion_order_date', 'issuing_authority', 'issuing_authority_id', 'employee', 'employee_id', 'promotion_value']

class SanctionOrderSerializer(serializers.ModelSerializer):
    issuing_authority = IssuingAuthoritySerializer(read_only=True)
    issuing_authority_id = serializers.PrimaryKeyRelatedField(queryset=IssuingAuthority.objects.all(), source='issuing_authority', write_only=True)
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)

    class Meta:
        model = SanctionOrder
        fields = ['sanction_order_id', 'sanction_order_no', 'sanction_order_date', 'issuing_authority', 'issuing_authority_id', 'employee', 'employee_id', 'sanction_value']

class PromotionSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)
    promotion_order = PromotionOrderSerializer(read_only=True)
    promotion_order_id = serializers.PrimaryKeyRelatedField(queryset=PromotionOrder.objects.all(), source='promotion_order', write_only=True)
    sanction_order = SanctionOrderSerializer(read_only=True)
    sanction_order_id = serializers.PrimaryKeyRelatedField(queryset=SanctionOrder.objects.all(), source='sanction_order', write_only=True)

    class Meta:
        model = Promotion
        fields = ['promotion_id', 'employee', 'employee_id', 'promotion_order', 'promotion_order_id', 'sanction_order', 'sanction_order_id', 'promotion_date']
