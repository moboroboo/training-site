from django.shortcuts import render
from django.http import HttpResponse

def blog_view(request):
    return render(request, 'blog/blog_list.html')

def single_blog(request):
    return render(request, 'blog/blog_detail.html')
