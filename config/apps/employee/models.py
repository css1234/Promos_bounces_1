from django.db import models

class Degree(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=255, verbose_name="Degree Name")
    start_stage_id = models.IntegerField(verbose_name="Start Stage ID")
    end_stage_id = models.IntegerField(verbose_name="End Stage ID")

    class Meta:
        verbose_name = "Degree"
        verbose_name_plural = "Degrees"

    def __str__(self):
        return self.degree_name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255, verbose_name="Employee Name")
    degree = models.ForeignKey(
        Degree,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
        verbose_name="Degree"
    )
    appointment_date = models.DateTimeField(verbose_name="Appointment Date")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.employee_name