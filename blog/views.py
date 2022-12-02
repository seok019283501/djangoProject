from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import  Post, Video
from .form import PostForm,VideoPost
from django.shortcuts import redirect
from embed_video.backends import detect_backend
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts' : posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form' : form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def delete_list(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def video_list(request):
    video_list = Video.objects.all()
    return render(request,'blog/video_list.html',{'video_list':video_list})
def video_new(request):
    if request.method =='POST':
        VideoPost(request.POST).save()
        return redirect('video_list')
    else:
        VideoPost()
    return render(request,'blog/video_new.html')

def video_detail(request, video_id):
    videos = Video.objects.get(id=video_id)
    return render(request,'blog/video_detail.html',{'videos':videos})





