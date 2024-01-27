from django.shortcuts import render
from django.core.paginator import Paginator
from article.models import Article


def home_page(request):
    articles = Article.objects.order_by('-id')[:3]
    articles2 = Article.objects.order_by('-id')[3:9:]
    # print(articles2)
    paginator = Paginator(articles, 3)
    # page_obj = paginator.get_page('page')
    page = request.GET.get('page')
    ctx = {
        'articles': articles,
        'articles2': articles2,
    }

    return render(request, 'main/index.html', ctx)


def contact_page(request):

    ctx = {

    }
    return render(request, 'main/contact.html', ctx)


def category_page(request):
    ctx = {

    }
    return render(request, 'main/category.html', ctx)
