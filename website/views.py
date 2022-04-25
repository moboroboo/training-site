from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages
from blog.models import Post

def index_view(request):
    latest_posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    context = {'posts': latest_posts}
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'تماس شما با موفقیت ثبت شد')
        else:
            messages.add_message(request, messages.ERROR, 'لطفا مجدد تلاش کنید')

    return render(request, 'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'website/index.html')