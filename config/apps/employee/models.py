from django.db import models

class Degree(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_name = models.CharField(max_length=255)
    start_stage_id = models.IntegerField()
    end_stage_id = models.IntegerField()

    def __str__(self):
        return self.degree_name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return self.employee_name