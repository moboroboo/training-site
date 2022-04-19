from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('post-<int:pid>', blog_detail, name='blog_detail')
]