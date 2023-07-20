from django import forms
from food.models import Food, Calorie


class FoodForm(forms.Form):
    food_calorie = forms.CharField(max_length=5, label="음식 칼로리", required=True)
    food_name = forms.CharField(max_length=20, label="음식 이름", required=True)

    class Meta:
        model = Food()
        fields = ['food_calorie','food_name']


class CalorieForm(forms.Form):
    health_calorie = forms.CharField(max_length=5, label="소비한 칼로리", required=True)
    eat_calorie = forms.CharField(max_length=5, label="섭취 칼로리", required=True)

    class Meta:
        model = Calorie()
        field = ['health_calorie']