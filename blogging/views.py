from django.shortcuts import render
from blogging.models import *


def index(request):
    blogs = blog.objects.order_by('-date_time')
    return render(request, 'index.html', {
        'blogs':blogs,
    })

def blog_detail(request, slug):
    article = blog.objects.get(slug=slug)
    uploads = article.uploads.all()
    return render(request, 'blogs/blog_detail.html', {
        'article': article,
        'uploads': uploads,
    })
