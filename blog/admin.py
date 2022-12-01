from django.contrib import admin
from .models import Post, Video
from embed_video.admin import AdminVideoMixin
# Register your models here.
admin.site.register(Post)
admin.site.register(Video)
