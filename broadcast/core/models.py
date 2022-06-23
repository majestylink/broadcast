from django.db import models

from embed_video.fields import EmbedVideoField

from accounts.models import CustomUser


class Broadcast(models.Model):
    NEWS = 'News'
    SPORTS = 'Sports'
    COMEDY = 'Comedy'
    broadcast_types = (
        (NEWS, "news"),
        (SPORTS, "sports"),
        (COMEDY, "comedy"),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = EmbedVideoField()
    genre = models.CharField(choices=broadcast_types, max_length=256, default=NEWS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
