from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog_list'),
    path('single-blog/', single_blog, name='single_detail'),
]