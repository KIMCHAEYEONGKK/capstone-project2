from django.shortcuts import render

# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.shortcuts import render
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import time

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

def health_first(request):
    videos_info = get_youtube_videos('바벨로우')
    videos_info1 = get_youtube_videos('데드리프트')
    videos_info2 = get_youtube_videos('렛풀다운')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/first.html', context)

def health_second(request):
    videos_info = get_youtube_videos('인클라인 벤치 프레스')
    videos_info1 = get_youtube_videos('플랫 벤치 프레스')
    videos_info2 = get_youtube_videos('인클라인 덤벨 플라이')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/second.html', context)

def health_third(request):
    videos_info = get_youtube_videos('스쿼트')
    videos_info1 = get_youtube_videos('런지')
    videos_info2 = get_youtube_videos('레그프레스')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/third.html', context)

def health_four(request):
    videos_info = get_youtube_videos('시티드 덤벨 프레스')
    videos_info1 = get_youtube_videos('프론트 덤벨 프레스')
    videos_info2 = get_youtube_videos('덤벨 래터럴 레이즈')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/four.html', context)

def health_five(request):
    videos_info = get_youtube_videos('덤벨 컬')
    videos_info1 = get_youtube_videos('바벨 컬')
    videos_info2 = get_youtube_videos('트라이셉스 푸시다운')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/five.html', context)

def health_six(request):
    videos_info = get_youtube_videos('등 스트레칭')
    videos_info1 = get_youtube_videos('햄스트링 스트레칭')
    videos_info2 = get_youtube_videos('허리 스트레칭')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/six.html', context)

def health_seven(request):
    videos_info = get_youtube_videos('동적 스트레칭')
    videos_info1 = get_youtube_videos('수동적 스트레칭')
    videos_info2 = get_youtube_videos('근막 이완 스트레칭')
    context = {'videos_info': videos_info, 'videos_info1': videos_info1,'videos_info2': videos_info2}
    return render(request, 'health/seven.html', context)