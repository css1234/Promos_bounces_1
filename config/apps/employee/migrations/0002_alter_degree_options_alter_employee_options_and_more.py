# Generated by Django 5.0.13 on 2025-04-03 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degree',
            options={'verbose_name': 'Degree', 'verbose_name_plural': 'Degrees'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='degree',
            name='degree_name',
            field=models.CharField(max_length=255, verbose_name='Degree Name'),
        ),
        migrations.AlterField(
            model_name='degree',
            name='end_stage_id',
            field=models.IntegerField(verbose_name='End Stage ID'),
        ),
        migrations.AlterField(
            model_name='degree',
            name='start_stage_id',
            field=models.IntegerField(verbose_name='Start Stage ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='appointment_date',
            field=models.DateTimeField(verbose_name='Appointment Date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='employee.degree', verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(max_length=255, verbose_name='Employee Name'),
        ),
    ]
