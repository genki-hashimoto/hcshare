from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from . import json_parse
from django.shortcuts import redirect



def post_list(request):
  posts = Post.objects.filter(registed_date__lte=timezone.now()).order_by('like')
  return render(request, 'mixshare/post_list.html', {'posts': posts})

def post_new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      key = post.url.replace("https://www.mixcloud.com/","")
      status = json_parse.json_parse(key)
      if status != False:
        post.url = key
        post.like = int(status[0])
        post.repost = int(status[1])
        post.play = int(status[2])
        post.save()
        return redirect('post_list')
      else:
        form = PostForm()
  else:
    form = PostForm()
  return render(request, 'mixshare/post_new.html', {'form': form})
