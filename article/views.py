from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from article.models import Article, Tag, Category


def article_list_page(request):
    object_list = Article.objects.order_by('-id')
    top_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-id')[:3]
    categories = Category.objects.all()
    print(categories)
    tags = Tag.objects.all()
    ctx = {
        "object_list": object_list,
        "top_articles": top_articles,
        "categories": categories,
        "tags": tags,
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
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        objects = Article.objects.filter(q).order_by('-id')
    if cat:
        objects = objects.filter(category__title__exact=cat)
    if tag:
        objects = objects.filter(category__title__exact=tag)
    ctx = {
        "objects": objects,
        "last_three": last_three,
        "categories": categories,
        "tags": tags,

    }
    return render(request, 'main/category.html', ctx)


