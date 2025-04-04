from rest_framework import serializers

from .models import Stage, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'
        read_only_fields = ['step_id']

class StageSerializer(serializers.ModelSerializer):
    step = StepSerializer(read_only=True)
    step_id = serializers.PrimaryKeyRelatedField(
        queryset=Step.objects.all(),
        source='step',
        write_only=True,
        label="Step ID")

    class Meta:
        model = Stage
        fields = ['stage_id', 'stage_name', 'step', 'step_id']
        read_only_fields = ['stage_id']