from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_list(request):
    published_posts = Post.objects.filter(status=True)
    context = {'posts': published_posts}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request,pid):
    published_posts = Post.objects.filter(status=True)
    post = get_object_or_404(published_posts, id=pid)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)
