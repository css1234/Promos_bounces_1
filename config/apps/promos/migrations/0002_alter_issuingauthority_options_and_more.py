# Generated by Django 5.0.13 on 2025-04-03 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_degree_options_alter_employee_options_and_more'),
        ('promos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuingauthority',
            options={'verbose_name': 'Issuing Authority', 'verbose_name_plural': 'Issuing Authorities'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'verbose_name': 'Promotion', 'verbose_name_plural': 'Promotions'},
        ),
        migrations.AlterModelOptions(
            name='promotionorder',
            options={'verbose_name': 'Promotion Order', 'verbose_name_plural': 'Promotion Orders'},
        ),
        migrations.AlterModelOptions(
            name='sanctionorder',
            options={'verbose_name': 'Sanction Order', 'verbose_name_plural': 'Sanction Orders'},
        ),
        migrations.AlterField(
            model_name='issuingauthority',
            name='issuing_authority_name',
            field=models.CharField(max_length=255, verbose_name='Issuing Authority Name'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_promotion', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='promotion_date',
            field=models.DateTimeField(verbose_name='Promotion Date'),
        ),
        migrations.AlterField(
            model_name='promotionorder',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='promotionorder',
            name='issuing_authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issuing_authority', to='promos.issuingauthority', verbose_name='Issuing Authority'),
        ),
        migrations.AlterField(
            model_name='promotionorder',
            name='promotion_order_date',
            field=models.DateTimeField(verbose_name='Promotion Order Date'),
        ),
        migrations.AlterField(
            model_name='promotionorder',
            name='promotion_order_no',
            field=models.CharField(max_length=255, verbose_name='Promotion Order No'),
        ),
        migrations.AlterField(
            model_name='promotionorder',
            name='promotion_value',
            field=models.IntegerField(verbose_name='Promotion Value'),
        ),
        migrations.AlterField(
            model_name='sanctionorder',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_sanction', to='employee.employee', verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='sanctionorder',
            name='issuing_authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issuing_authority_sanction', to='promos.issuingauthority', verbose_name='Issuing Authority'),
        ),
        migrations.AlterField(
            model_name='sanctionorder',
            name='sanction_order_date',
            field=models.DateTimeField(verbose_name='Sanction Order Date'),
        ),
        migrations.AlterField(
            model_name='sanctionorder',
            name='sanction_order_no',
            field=models.CharField(max_length=255, verbose_name='Sanction Order No'),
        ),
        migrations.AlterField(
            model_name='sanctionorder',
            name='sanction_value',
            field=models.IntegerField(verbose_name='Sanction Value'),
        ),
    ]
