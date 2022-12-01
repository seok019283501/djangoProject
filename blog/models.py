from django.db import models #다른파일에 있는 것을 추가하라는 뜻
from django.conf import settings
from django.utils import timezone
from embed_video.fields import EmbedVideoField
# Create your models here.

class Post(models.Model): #모델을 정의하는 코드
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)#다른 모델에 대한 링크를 의미
    title = models.CharField(max_length=200)#글자수가 제한된 텍스트를 정의 할 때 사용 글 제목같이 짧은 문자열 정보를 저장할때 사용
    text = models.TextField()# 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    create_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null = True
    )
    def publich(self):# 게시일 함수
        self.publiched_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200,default='')
    video_key = EmbedVideoField()