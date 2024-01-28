from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from article.models import Article, Tag, Category


def article_list_page(request):
    object_list = Article.objects.order_by('-id')
    top_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-id')[:3]
    categories = Category.objects.all()
    categories_count = {}
    for category in categories:
        count = Article.objects.filter(category=category).count()
        categories_count[category.title] = count
    tags = Tag.objects.all()
    ctx = {
        "object_list": object_list,
        "top_articles": top_articles,
        "categories": categories,
        "categories_count": categories_count,
        "tags": tags
    }
    return render(request, 'article/archive.html', ctx)


def single_blog_page(request, slug):
    article = get_object_or_404(Article, slug=slug)
    ctx = {
        "object": article,
    }
    return render(request, 'article/single-blog.html', ctx)


def category_page(request):
    objects = Article.objects.order_by('-id')
    last_three = objects[3:]
    categories = Category.objects.all()
    category_counts = {}
    print(category_counts)
    for category in categories:
        count = Article.objects.filter(category=category).count()
        category_counts[category.title] = count
    ctx = {
        "objects": objects,
        "last_three": last_three,
        "category_counts": category_counts,
    }
    return render(request, 'main/category.html', ctx)


def tag_page(request):
    tags = Tag.objects.all()
    print(tags)
    ctx = {
        "tags": tags,
    }
    return render(request, 'main/category.html', ctx)