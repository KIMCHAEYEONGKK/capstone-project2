from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CalorieForm
from .models import Calorie,Food
from django.shortcuts import render
from googleapiclient.discovery import build


@login_required(login_url="common:login")
def request_Calorie(request):
    if request.method == 'POST':
        form = CalorieForm(request.POST)
        if form.is_valid():
            calorie = Calorie()
            # food = Food()
            # calorie.eat_calorie = sum(food.food_calorie)
            calorie.health_calorie = form.cleaned_data['health_calorie']
            calorie.user = request.user  # 현재 로그인한 사용자의 id
            calorie.eat_calorie = form.cleaned_data['eat_calorie']
            # calorie.eat_calorie = Food.objects.aggregate(Sum('food_calorie'))
            calorie.save()

            return HttpResponseRedirect('/common/index')  # 작성 후 글목록으로 이동
        else:
            return render(request, 'food/food.html')
    else:
        form = CalorieForm()
    return render(request, 'food/food.html', {'form': form})


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


def food(request):
    videos_info = get_youtube_videos('닭가슴살 다이어트 요리')
    videos_info1 = get_youtube_videos('두부 다이어트 요리')
    videos_info2 = get_youtube_videos('달걀 다이어트 요리')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1, 'videos_info2': videos_info2}
    return render(request, 'food/food_menu.html', context)


# @login_required(login_url="common:login")
# def food_update(request):
#     cal = Calorie.objects.get(user=request.user)
#     if request.method == "POST":
#         cal.weight = request.POST.get('weight')
#         cal.muscle = request.POST.get('muscle')
#         cal.fat = request.POST.get('fat')
#         cal.target_weight = request.POST.get('target_weight')
#         cal.user = request.user
#         cal.save()
#         return redirect('/common/index/')
#     else:
#         calorieForm = CalorieForm()
#         return render(request, 'setting/inbody_update.html', {'calorieForm':calorieForm})