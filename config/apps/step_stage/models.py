from django.db import models


class Step(models.Model):
    step_id = models.AutoField(primary_key=True)
    step_name = models.CharField(max_length=255,verbose_name="Step Name")
    step_duration = models.IntegerField(verbose_name="Step Duration (days)")
    
    class Meta:
        verbose_name = "Step"
        verbose_name_plural = "Steps"

    def __str__(self):
        return self.step_name

class Stage(models.Model):
    stage_id = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=255 ,verbose_name="Stage Name")
    step = models.ForeignKey(
        Step, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stages",
        verbose_name="Step")
    
    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

    def __str__(self):
        return self.stage_name
