from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from article.models import Article, Category, Tag
from .models import Contact
from .form import ContactForm
from django.contrib import messages


def home_page(request):
    articles = Article.objects.order_by('-id')
    articles1 = Article.objects.order_by('-id')[:3]
    articles2 = Article.objects.order_by('-id')[3:9:]
    categories = Category.objects.all()
    tags = Tag.objects.all()

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
    }

    return render(request, 'main/index.html', ctx)


def contact_page(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting")
            return redirect('.')
    ctx = {
        "form": form,
    }
    return render(request, 'main/contact.html', ctx)


