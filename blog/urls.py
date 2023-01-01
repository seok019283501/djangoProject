from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('delete/<int:pk>/',views.delete_list,name='delete_list'),
    path('video/', views.video_list,name='video_list'),
    path('video/new/',views.video_new,name='video_new'),
    path('video/<int:video_id>/',views.video_detail,name='video_detail'),
    path('video/delete/<int:video_id>/',views.video_delete,name='video_delete')
]#post_list라는 view가 루트 url에 할당되었습니다. name은 url에 이름을 붙인것으로 뷰를 식별한다.
