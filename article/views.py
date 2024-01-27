from django.shortcuts import render, get_object_or_404
from article.models import Article


def article_list_page(request):
    articles = Article.objects.order_by('-id')
    ctx = {
        "object": articles
    }
    return render(request, 'article/archive.html', ctx)


def single_blog_page(request, slug):
    article = get_object_or_404(Article, slug=slug)
    ctx = {
        "object": article,
    }
    return render(request, 'article/single-blog.html', ctx)