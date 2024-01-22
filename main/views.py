from django.shortcuts import render

def home_page(request):
    ctx = {

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
