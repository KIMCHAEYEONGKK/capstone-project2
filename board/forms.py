from django import forms
from .models import Board
# from django_summernote.fields import SummernoteTextField
# from django_summernote.widgets import SummernoteWidget


class BoardForm(forms.ModelForm):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        max_length=100, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요'  # 입력하지 않은 경우('required'키에 저장) 에러메시지 지정
        },
        widget=forms.Textarea, label="내용")  # 내용를 입력할 위젯을 지정

    field_order = ['title','contents']

    class Meta:
        model = Board
        fields = ['title','contents']
        exclude =['writer',]




