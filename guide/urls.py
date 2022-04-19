from django.urls import path
from guide.views import *

app_name = 'guide'

urlpatterns = [
    path('', guide_view, name='guide_list'),
    path('paper-<int:pid>', single_guide, name='guide_detail')
]