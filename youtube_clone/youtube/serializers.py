from django.db import models
from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_id', 'comment', 'likes', 'dislikes', 'replies']
