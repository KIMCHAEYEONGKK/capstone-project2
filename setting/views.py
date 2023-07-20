from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Setting
from setting.forms import SettingForm
from common.models import Common


@login_required(login_url="common:login")
def inbody(request):
    if request.method == 'POST':
        form = SettingForm(request.POST)
        if form.is_valid():
            Set = Setting()  # 모델 클래스 변수 생성
            Set.weight = form.cleaned_data['weight']  # form의 제목을 가져옴
            Set.fat = form.cleaned_data['fat']
            Set.muscle = form.cleaned_data['muscle']
            Set.target_weight = form.cleaned_data['target_weight']
            Set.user = request.user  # 현재 로그인한 사용자의 id
            Set.save()
            return HttpResponseRedirect('/food/food/')  # 작성 후 글목록으로 이동
        else:
            return render(request, 'setting/inbody.html')
    else:
        form = SettingForm()
    return render(request, 'setting/inbody.html', {'form': form})


# @login_required(login_url="common:login")
# def inbody_update(request):
#     Set = Setting.objects.get(user=request.user)
#     if request.method == "POST":
#         Set.weight = request.POST.get('weight')
#         Set.muscle = request.POST.get('muscle')
#         Set.fat = request.POST.get('fat')
#         Set.target_weight = request.POST.get('target_weight')
#         Set.user = request.user
#         Set.save()
#         return redirect('/food/food/')
#     else:
#         settingForm = SettingForm(instance = Set)
#         return render(request, 'setting/inbody_update.html', {'settingForm':settingForm})
#

@login_required(login_url="common:login")
def inbody_list(request):
    sets = Setting.objects.all().order_by('-id')
    return render(request, 'setting/inbody_list.html', {'sets': sets})

