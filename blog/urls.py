from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog_view),
    path('single-blog/', single_blog),
]