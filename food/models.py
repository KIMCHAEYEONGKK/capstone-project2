from django.db import models
from common.models import Common
from django.db.models import Sum


# Create your models here.


class Food(models.Model):
    objects = None
    food_name = models.CharField(max_length=100, verbose_name="음식 이름")
    food_calorie = models.CharField(max_length=5, verbose_name="음식 칼로리")

    USERNAME_FIELD = "food_name"

    def __str__(self):
        return f"{self.food_name} ({self.food_calorie})kcal"




    class Meta:
        db_table = "UserFood"
        verbose_name = "food"


class Calorie(models.Model):
    objects = None
    user = models.OneToOneField('common.Common', on_delete=models.CASCADE, verbose_name="사용자")
    health_calorie = models.CharField(max_length=5, verbose_name="소비한 칼로리")
    eat_calorie = models.CharField(max_length=5, verbose_name="섭취한 칼로리")

    class Meta:
        db_table = "UserCalorie"
        verbose_name = "calorie"
