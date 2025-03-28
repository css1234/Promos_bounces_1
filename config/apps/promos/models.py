from django.db import models
from apps.employee.models import Employee

class IssuingAuthority(models.Model): 
    issuing_authority_id = models.AutoField(primary_key=True)
    issuing_authority_name = models.CharField(max_length=255)

    def __str__(self):
        return self.issuing_authority_name  

class PromotionOrder(models.Model):
    promotion_order_id = models.AutoField(primary_key=True)
    promotion_order_no = models.CharField(max_length=255)
    promotion_order_date = models.DateTimeField()
    issuing_authority = models.ForeignKey(IssuingAuthority, on_delete=models.SET_NULL, null=True, blank=True , related_name='issuing_authority')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    promotion_value = models.IntegerField()

    def __str__(self):
        return self.promotion_order_no  
    
class SanctionOrder(models.Model):
    sanction_order_id = models.AutoField(primary_key=True)
    sanction_order_no = models.CharField(max_length=255)
    sanction_order_date = models.DateTimeField()
    issuing_authority = models.ForeignKey(IssuingAuthority, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    sanction_value = models.IntegerField()

    def __str__(self):
        return self.sanction_order_no  

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    promotion_date = models.DateTimeField()

    def __str__(self):
        return f"{self.promotion_order.promotion_order_no} {self.sanction_order.sanction_order_no}"
