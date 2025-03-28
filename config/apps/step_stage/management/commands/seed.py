from django.core.management.base import BaseCommand
from apps.step_stage.models import Step, Stage  # Adjust according to your app name

class Command(BaseCommand):
    help = "Seed initial data for Step and Stage models"

    def handle(self, *args, **kwargs):
        # Seed Step data
        steps_data = [
            {"step_id": 1, "step_name": "الاولى", "step_duration": 5},
            {"step_id": 2, "step_name": "الثانية", "step_duration": 5},
            {"step_id": 3, "step_name": "الثالثة", "step_duration": 5},
            {"step_id": 4, "step_name": "الرابعة", "step_duration": 5},
            {"step_id": 5, "step_name": "الخامسة", "step_duration": 5},
            {"step_id": 6, "step_name": "السادسة", "step_duration": 4},
            {"step_id": 7, "step_name": "السابعة", "step_duration": 4},
            {"step_id": 8, "step_name": "الثامنة", "step_duration": 4},
            {"step_id": 9, "step_name": "التاسعة", "step_duration": 4},
            {"step_id": 10, "step_name": "العاشرة", "step_duration": 4},
        ]

        # Insert Steps
        for step_data in steps_data:
            step, created = Step.objects.get_or_create(step_id=step_data["step_id"], defaults=step_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Step created: {step.step_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Step already exists: {step.step_name}"))

        # Insert Stages (1 to 11 for each Step)
        for step in Step.objects.all():
            for i in range(1, 12):
                stage_name = i
                stage, created = Stage.objects.get_or_create(stage_id=(step.step_id - 1) * 11 + i, defaults={"stage_name": stage_name, "step": step})
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Stage created: {stage.stage_name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Stage already exists: {stage.stage_name}"))

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))

