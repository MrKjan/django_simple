import datetime
from django.shortcuts import render, get_object_or_404
from .models import Blogpost

def all_blogs(request):
    posts = Blogpost.objects.all()
    posts_count = Blogpost.objects.count
    # print(timedelta(milliseconds=1000) > posts[0].update_datetime - posts[0].creation_datetime)
    return render(request, 'blog/all_blogs.html', {'posts' : posts})

def detail(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog})
