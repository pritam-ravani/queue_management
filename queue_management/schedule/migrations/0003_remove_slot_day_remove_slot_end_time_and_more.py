# Generated by Django 5.0.2 on 2024-02-14 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_shift_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='day',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='shift',
            name='days',
            field=models.ManyToManyField(related_name='shifts', to='schedule.day'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='schedule.shift'),
        ),
    ]