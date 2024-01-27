from django.shortcuts import render
from django.core.paginator import Paginator
from article.models import Article, Category, Tag


def home_page(request):
    articles = Article.objects.order_by('-id')
    articles1 = Article.objects.order_by('-id')[:3]
    articles2 = Article.objects.order_by('-id')[3:9:]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    category_counts = {}

    for category in categories:
        count = Article.objects.filter(category=category).count()
        category_counts[category.title] = count
    # for i in
    # print(articles2)
    paginator = Paginator(articles1, 3)
    # page_obj = paginator.get_page('page')
    page = request.GET.get('page')
    ctx = {
        'articles': articles,
        'articles1': articles1,
        'articles2': articles2,
        'categories': categories,
        'tags': tags,
        'category_counts': category_counts,
    }

    return render(request, 'main/index.html', ctx)


def contact_page(request):

    ctx = {

    }
    return render(request, 'main/contact.html', ctx)


