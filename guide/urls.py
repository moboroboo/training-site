from django.urls import path
from guide.views import *

app_name = 'guide'

urlpatterns = [
    path('', guide_view, name='guide_list'),
    path('مقاله-<int:pid>', single_guide, name='guide_detail'),
    path('category/<str:cat_name>', guide_view, name='guide_category'),
    path('search/', guide_search, name='guide_search')
]