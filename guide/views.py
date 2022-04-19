from django.shortcuts import render, get_object_or_404
from guide.models import Paper

def guide_view(request):
    published_papers = Paper.objects.filter(status=True)
    context ={'papers': published_papers}
    return render(request, 'guide/guide_list.html', context)

def single_guide(request, pid):
    published_papers = Paper.objects.filter(status=True)
    paper = get_object_or_404(published_papers, id=pid)
    context = {'paper': paper}
    return render(request, 'guide/guide_detail.html', context)

