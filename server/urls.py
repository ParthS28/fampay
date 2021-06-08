from django.urls import path

from . import services
from . import views


urlpatterns = [
	path('get_videos/', views.GetVideos.as_view()),
    path('get_videos_title/', views.GetVideosBasedOnTitle.as_view()),
]


services.THREAD.start()