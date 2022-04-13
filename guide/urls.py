from django.urls import path
from guide.views import *

app_name = 'guide'

urlpatterns = [
    path('', guide_view, name='guide'),
    path('single-guide/', single_guide, name='single-guide')
]