# Generated by Django 5.0.2 on 2024-02-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='days',
            field=models.ManyToManyField(to='schedule.day'),
        ),
    ]
