import re

from django.apps import AppConfig
from  embed_video.backends import VideoBackend

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"