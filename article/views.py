from django.shortcuts import render

def article_list_page(request):

    ctx = {

    }
    return render(request, 'article/archive.html', ctx)


def single_blog_page(request, slug):

    ctx = {

    }
    return render(request, 'article/single-blog.html', ctx)