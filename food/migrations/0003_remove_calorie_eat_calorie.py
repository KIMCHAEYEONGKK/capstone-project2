# Generated by Django 4.1.7 on 2023-05-23 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_rename_user_id_calorie_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calorie',
            name='eat_calorie',
        ),
    ]