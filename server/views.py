import asyncio
import threading
from django import forms
from django.shortcuts import render

from rest_framework import generics, status, filters
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers
# Create your views here.


class GetVideosPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10


class GetVideos(generics.ListAPIView):
    """
    View for getting all the videos
    """
    renderer_classes = [JSONRenderer]
    serializer_class = serializers.VideoSerializer
    pagination_class = GetVideosPagination

    def get_queryset(self):
        return models.Video.objects.all().order_by('published_at')

class GetVideosBasedOnTitle(generics.ListAPIView):
    """
    View for getting all the videos, based on title, description or partial match with either title or description
    """
    renderer_classes = [JSONRenderer]
    search_fields = ['video_title', 'description', 'keywords']
    filter_backends = (filters.SearchFilter,)
    serializer_class = serializers.VideoSerializer
    def get_queryset(self):
        return models.Video.objects.all()

