from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Broadcast, Playlist


class BroadcastAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Broadcast, BroadcastAdmin)
admin.site.register(Playlist)
