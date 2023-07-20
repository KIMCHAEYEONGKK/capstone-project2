import random
import np as np
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreateForm, LoginForm
from setting.models import Setting
from food.models import Calorie,Food
from django.contrib.auth.models import User
from django.http import HttpResponse
from common.models import Common


def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            tall = form.cleaned_data.get('tall')
            gender = form.cleaned_data.get('gender')
            exercise = form.cleaned_data.get('exercise')
            weight_l = form.cleaned_data.get('weight_l')

            user = authenticate(username=username, password=password1, name=name,
                                age=age, exercise=exercise, tall=tall, gender=gender,weight_l=weight_l)

            login(request, user)
            return redirect('/common/login')
        else:
            return render(request, 'common/signup.html')
    else:
        form = UserCreateForm()

    return render(request, 'common/signup.html', {'form': form})


def view_login(request):
    response_data = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    sets = Setting.objects.get(user=request.user)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/setting/inbody')
    else:
        response_data['error'] = "비밀번호를 틀렸습니다."
    return render(request, 'common/login.html', response_data,{'sets':sets})


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/common/login')


def index(request):
    username = request.session.get('user')
    commons = Common.objects.get(username=request.user)
    sets = Setting.objects.get(user=request.user)
    cal = Calorie.objects.get(user=request.user)
    foods = Food.objects.all()
    food = random.choice(foods)
    food_1 = random.choice(foods)
    food_2 = random.choice(foods)
    food_3 = random.choice(foods)
    food_4 = random.choice(foods)
    food_5 = random.choice(foods)
    food_6 = random.choice(foods)
    food_7 = random.choice(foods)
    food_8 = random.choice(foods)
    if username:
        user = Common.objects.get(pk=username)
        return HttpResponse(f'{user} login success')
    context = {'sets': sets, 'cal': cal,'commons': commons,'food':food,'food_1':food_1,'food_2':food_2,'food_3':food_3,'food_4':food_4,'food_5':food_5,'food_6':food_6,'food_7':food_7, 'food_8':food_8}
    return render(request, 'common/index.html',context)


from django.shortcuts import render
from googleapiclient.discovery import build


def get_youtube_videos(keyword):
    # Build the YouTube API client.
    youtube = build('youtube', 'v3', developerKey='AIzaSyDBTva00FGQI39RXdl4FzCF1E7eTKo787I')

    # Send a video search request.
    response = youtube.search().list(
        part='snippet',
        q=keyword,
        type='video',
        maxResults=10
    ).execute()

    items = response.get('items', [])

    # Initialize a list to store video information.
    videos_info = []

    # Retrieve the title, thumbnail URL, and video URL for each video and add them to the list.
    for item in items:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        thumbnail_url = item['snippet']['thumbnails']['default']['url']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        videos_info.append({'title': title, 'thumbnail_url': thumbnail_url, 'video_url': video_url})

    return videos_info


def health(request):
    keyword = '등운동'  # Enter your desired keyword for the search query.
    videos_info = get_youtube_videos(keyword)
    return render(request, 'common/health_page.html', {'videos_info': videos_info})


def home(request):
    videos_info = get_youtube_videos('단기간 다이어트')
    videos_info1 = get_youtube_videos('다이어트 식단 추천')
    videos_info2 = get_youtube_videos('운동 추천')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1, 'videos_info2': videos_info2}
    return render(request, 'common/home.html', context)

