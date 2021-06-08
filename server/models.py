from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.CharField(max_length=20)
    video_title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)
    thumbnail_url = models.URLField(max_length=200)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    keywords = models.CharField(max_length=1000, default='')

    class Meta:
        verbose_name = "Video details"
