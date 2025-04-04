# Generated by Django 5.0.13 on 2025-04-03 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('step_stage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': 'Stage', 'verbose_name_plural': 'Stages'},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'verbose_name': 'Step', 'verbose_name_plural': 'Steps'},
        ),
        migrations.AlterField(
            model_name='stage',
            name='stage_name',
            field=models.CharField(max_length=255, verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stages', to='step_stage.step', verbose_name='Step'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_duration',
            field=models.IntegerField(verbose_name='Step Duration (days)'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_name',
            field=models.CharField(max_length=255, verbose_name='Step Name'),
        ),
    ]
