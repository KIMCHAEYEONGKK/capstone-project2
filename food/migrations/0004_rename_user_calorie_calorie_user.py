# Generated by Django 4.1.7 on 2023-05-23 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_calorie_eat_calorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calorie',
            old_name='user',
            new_name='calorie_user',
        ),
    ]
