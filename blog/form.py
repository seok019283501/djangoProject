from django import forms
from .models import Post,Video
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text',)
class VideoPost(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title','video_key')