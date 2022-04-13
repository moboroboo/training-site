from django.urls import path
from guide.views import *

urlpatterns = [
    path('', guide_view),
    path('single-guide/', single_guide),
]