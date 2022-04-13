from django.shortcuts import render
from django.http import HttpResponse

def guide_view(request):
    return render(request, 'guide/guide_list.html')

def single_guide(request):
    return render(request, 'guide/guide_detail.html')

