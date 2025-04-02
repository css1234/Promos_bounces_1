from django.core.management.base import BaseCommand
from apps.step_stage.models import Step, Stage

class Command(BaseCommand):
    help = "Seed initial Step and Stage data into the database"

    def handle(self, *args, **kwargs):
        # Step Names
        step_names = ["الاولى", "الثانية", "الثالثة", "الرابعة", "الخامسة", 
                  "السادسة", "السابعة", "الثامنة", "التاسعة", "العاشرة"]
        step_durations = [5, 5, 5, 5, 5, 4, 4, 4, 4, 4]
        
        steps = zip(step_names, step_durations)

        self.stdout.write(self.style.SUCCESS("Seeding Steps..."))
        
        step_instances = []
        for name, step_duration in steps:
            step, created = Step.objects.get_or_create(
                step_name=name, 
                step_duration=step_duration
            )
            step_instances.append(step)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Step: {name}"))

        self.stdout.write(self.style.SUCCESS("Seeding Stages..."))

        for step in step_instances:
            for i in range(1, 12):  # Stage names from 1 to 11
                stage, created = Stage.objects.get_or_create(
                    stage_name=str(i), 
                    step=step
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created Stage {i} for Step {step.step_name}"))

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully!"))
