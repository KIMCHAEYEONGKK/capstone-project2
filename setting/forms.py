from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from setting.models import Setting


class SettingForm(forms.ModelForm):
    weight = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="체중")
    fat = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="체지방량")
    muscle = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="골격근량")
    target_weight = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=20, label="목표체중")

    field_order = ["weight", "fat", "muscle", "target_weight"]

    class Meta:
        model = Setting
        fields = ["weight", "fat", "muscle", "target_weight"]
        exclude =['user']

#
# class CustomUserChangeForm(UserChangeForm):
#     password = None
#
#     weight = forms.CharField(label="체중",widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'max_length':'5','oninput':"maxLengthCheck(this)", }
#     ), )
#     fat = forms.CharField(label="체지방량", widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'max_length': '5', 'oninput': "maxLengthCheck(this)", }
#     ), )
#     muscle = forms.CharField(label="골격근량", widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'max_length': '5', 'oninput': "maxLengthCheck(this)", }
#     ), )
#     target_weight = forms.CharField(label="목표체중", widget=forms.NumberInput(
#         attrs={'class': 'form-control', 'max_length': '5', 'oninput': "maxLengthCheck(this)", }
#     ), )
#
#     class Meta:
#         model = Setting()
#         fields = ['weight','fat','muscle','target_weight']
#
