from django.db import models

from apps.employee.models import Employee


class IssuingAuthority(models.Model): 
    issuing_authority_id = models.AutoField(primary_key=True)
    issuing_authority_name = models.CharField(max_length=255 , verbose_name="Issuing Authority Name")

    class Meta:
        verbose_name = "Issuing Authority"
        verbose_name_plural = "Issuing Authorities"

    def __str__(self):
        return self.issuing_authority_name  

class PromotionOrder(models.Model):
    promotion_order_id = models.AutoField(primary_key=True)
    promotion_order_no = models.CharField(max_length=255 , verbose_name="Promotion Order No")
    promotion_order_date = models.DateTimeField(verbose_name="Promotion Order Date")
    issuing_authority = models.ForeignKey(
        IssuingAuthority, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True , 
        related_name='issuing_authority',
        verbose_name="Issuing Authority")
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='employee',
        verbose_name="Employee")
    promotion_value = models.IntegerField(verbose_name="Promotion Value")
    
    class Meta:
        verbose_name = "Promotion Order"
        verbose_name_plural = "Promotion Orders"

    def __str__(self):
        return self.promotion_order_no  
    
class SanctionOrder(models.Model):
    sanction_order_id = models.AutoField(primary_key=True)
    sanction_order_no = models.CharField(max_length=255 , verbose_name="Sanction Order No")
    sanction_order_date = models.DateTimeField(verbose_name="Sanction Order Date")
    issuing_authority = models.ForeignKey(
        IssuingAuthority,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='issuing_authority_sanction',
        verbose_name="Issuing Authority")
    
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='employee_sanction',
        verbose_name="Employee")
    sanction_value = models.IntegerField(verbose_name="Sanction Value")

    class Meta:
        verbose_name = "Sanction Order"
        verbose_name_plural = "Sanction Orders"

    def __str__(self):
        return self.sanction_order_no  

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='employee_promotion',
        verbose_name="Employee")
    
    promotion_date = models.DateTimeField(verbose_name="Promotion Date")

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return f"{self.promotion_order.promotion_order_no} {self.sanction_order.sanction_order_no}"
