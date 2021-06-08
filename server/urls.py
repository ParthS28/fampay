from django.urls import path

from . import services
from . import views

"""
We have two types of urls, first one is to get all the videos in date order and the
second one is to search title or description. 
"""
urlpatterns = [
	path('get_videos/', views.GetVideos.as_view()),
    path('get_videos_title/', views.GetVideosBasedOnTitle.as_view()),
]


services.THREAD.start()