from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.TextField(max_length=150)
    comment = models.TextField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    replies = models.TextField(blank=True, null=True, max_length=150)
