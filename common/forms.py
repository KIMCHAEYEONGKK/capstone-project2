from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Common

# GENDER_CHOICES = (
#     ("여자", "여자"), ("남자", "남자"),
# )


EXERCISE_EVERYDAY = "every"
EXERCISE_ONCE = "one"
EXERCISE_THREE = "three"
EXERCISE_FOUR = "four"
EXERCISE_NO = "no"

EXERCISE_CHOICES = (
    (EXERCISE_EVERYDAY, '일주일에 운동을 매일 합니다.'),
    (EXERCISE_FOUR, '일주일에 4~5번합니다.'),
    (EXERCISE_THREE, '일주일에 3~4번합니다.'),
    (EXERCISE_ONCE, '일주일에 1~2번합니다.'),
    (EXERCISE_NO, '일주일에 운동을 안합니다.')
)

class UserCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=20, label="이름", required=True)
    age = forms.CharField(max_length=20, label="나이", required=True)
    tall = forms.CharField(max_length=20, label="키", required=True)
    # exercise = forms.CharField(max_length=20, label="운동여부",
    #                            widget=forms.Select(choices=EXERCISE_CHOICES), required=True)
    # gender = forms.CharField(label="성별",
    #                          widget=forms.Select(choices=GENDER_CHOICES))

    gender = forms.CharField(max_length=10, label="성별", required=True)
    exercise = forms.CharField(max_length=100,label="운동 여부", required=True)
    username = forms.CharField(max_length=20, label='아이디', required=True)
    password1 = forms.CharField(max_length=20, label='비밀번호', required=True)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label="비밀번호 확인")

    class Meta:
        model = Common
        fields = ("username", "name", "password1", "password2", "tall", "age","gender","exercise")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Common
        fields = ('username', 'password', 'name', 'age', 'tall','gender','exercise')

    def clean_password(self):
        return self.initial['password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="아이디")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
