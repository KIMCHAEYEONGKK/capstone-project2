# Generated by Django 4.1.7 on 2023-05-30 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0006_calorie_eat_calorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calorie',
            name='calorie_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
            preserve_default=False,
        ),
    ]
