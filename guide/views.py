from django.shortcuts import render, get_object_or_404
from guide.models import Paper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def guide_view(request, cat_name=None):
    published_papers = Paper.objects.filter(status=True)
    if cat_name:
        published_papers = published_papers.filter(category__name=cat_name)

    published_papers= Paginator(published_papers, 4)
    try:
        page_number = request.GET.get('page')
        published_papers = published_papers.page(page_number)
    except EmptyPage:
        published_papers = published_papers.page(1)
    except PageNotAnInteger:
        published_papers = published_papers.page(1)
    
    context ={'papers': published_papers}
    return render(request, 'guide/guide_list.html', context)

def single_guide(request, pid):
    published_papers = Paper.objects.filter(status=True)
    paper = get_object_or_404(published_papers, id=pid)
    context = {'paper': paper}
    return render(request, 'guide/guide_detail.html', context)

def guide_search(request):
    published_papers = Paper.objects.filter(status=True)

    if request.method == 'GET':
        published_papers = published_papers.filter(content__contains=request.GET.get('s'))

    context = {'papers': published_papers}
    return render(request, 'guide/guide_list.html', context)
