# Generated by Django 5.0.2 on 2024-03-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_enduser_remove_user_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='is_enduser',
            field=models.BooleanField(default=False),
        ),
    ]