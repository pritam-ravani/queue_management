# Generated by Django 5.0.2 on 2024-02-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]
