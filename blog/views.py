from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_list(request, cat_name=None, author_username=None):
    published_posts = Post.objects.filter(status=True)
    if cat_name:
        published_posts = published_posts.filter(category__name=cat_name)
    if author_username:
        published_posts = published_posts.filter(author__username=author_username)
    
    published_posts = Paginator(published_posts, 4)
    try:
        page_number = request.GET.get('page')
        published_posts = published_posts.page(page_number)
    except EmptyPage:
        published_posts = published_posts.page(1)
    except PageNotAnInteger:
        published_posts = published_posts.page(1)

    context = {'posts': published_posts}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request,pid):
    published_posts = Post.objects.filter(status=True)
    post = get_object_or_404(published_posts, id=pid)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)

def blog_search(request):
    published_posts = Post.objects.filter(status=True)

    if request.method == 'GET':
        published_posts = published_posts.filter(content__contains=request.GET.get('s'))
        
    context = {'posts': published_posts}
    return render(request, 'blog/blog_list.html', context)
