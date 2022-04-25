from django import template
from blog.models import Post, Category


register = template.Library()

@register.inclusion_tag('blog/blog_recent_posts.html')
def latest_posts(n = 3):
    posts = Post.objects.filter(status=True).order_by('-published_date')[:n]
    return {'posts': posts}

@register.inclusion_tag('blog/blog_category.html')
def categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    dict = {}
    for name in categories:
        dict[name] = posts.filter(category=name).count()

    return {'categories': dict}
