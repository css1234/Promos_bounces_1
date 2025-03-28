from rest_framework import serializers
from .models import Step, Stage

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    step = StepSerializer(read_only=True)
    step_id = serializers.PrimaryKeyRelatedField(queryset=Step.objects.all(), source='step', write_only=True)

    class Meta:
        model = Stage
        fields = ['stage_id', 'stage_name', 'step', 'step_id']