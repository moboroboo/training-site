from django import template
from guide.models import Paper, Category


register = template.Library()

@register.inclusion_tag('guide/guide_recent_papers.html')
def latest_posts(n = 3):
    papers = Paper.objects.filter(status=True).order_by('-published_date')[:n]
    return {'papers': papers}

@register.inclusion_tag('guide/guide_category.html')
def categories():
    papers = Paper.objects.filter(status=True)
    categories = Category.objects.all()
    dict = {}
    for name in categories:
        dict[name] = papers.filter(category=name).count()

    return {'categories': dict}