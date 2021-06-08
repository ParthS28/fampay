from rest_framework import serializers

from . import models
from . import services

class VideoSerializer(serializers.ModelSerializer):
    """Serializer for Video Model."""
    class Meta:
        model = models.Video
        fields = '__all__'
