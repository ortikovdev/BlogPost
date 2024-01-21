from django.shortcuts import render

def home_page(request):
    ctx = {

    }
    return render(request, 'main/index.html', ctx)

def archive_page(request):
    objects = request.GET.get('objects')
    ctx = {
        "objects_list": objects
    }
    return render(request, 'main/archive.html', ctx)


def contact_page(request):

    ctx = {

    }
    return render(request, 'main/contact.html', ctx)