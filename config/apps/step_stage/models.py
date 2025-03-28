from django.db import models

class Step(models.Model):
    step_id = models.AutoField(primary_key=True)
    step_name = models.CharField(max_length=255)
    step_duration = models.IntegerField()

    def __str__(self):
        return self.step_name

class Stage(models.Model):
    stage_id = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=255)
    step = models.ForeignKey(Step, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.stage_name
