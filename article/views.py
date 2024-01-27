from django.shortcuts import render, get_object_or_404
from article.models import Article, Tag, Category


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


def category_page(request):
    categories = Category.objects.all()
    print(categories)
    ctx = {
        "categories": categories
    }
    return render(request, 'main/category.html', ctx)


def tag_page(request):
    tags = Tag.objects.all()
    ctx = {
        "tags": tags,
    }
    return render(request, '')