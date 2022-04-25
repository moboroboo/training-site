from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('post-<int:pid>', blog_detail, name='blog_detail'),
    path('category/<str:cat_name>', blog_list, name='blog_category'),
    path('author/<str:author_username>', blog_list, name='blog_author'),
    path('search/', blog_search, name='blog_search')
]