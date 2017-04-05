from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(registed_date__lte=timezone.now()).order_by('like')
    return render(request, 'mixshare/post_list.html', {'posts': posts})
