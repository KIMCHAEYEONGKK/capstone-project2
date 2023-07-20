# Generated by Django 4.1.7 on 2023-05-19 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100, verbose_name='음식 이름')),
                ('food_calorie', models.CharField(max_length=5, verbose_name='음식 칼로리')),
            ],
            options={
                'verbose_name': 'food',
                'db_table': 'UserFood',
            },
        ),
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_calorie', models.CharField(max_length=5, verbose_name='소비한 칼로리')),
                ('eat_calorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='섭취한 칼로리')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': 'calorie',
                'db_table': 'UserCalorie',
            },
        ),
    ]