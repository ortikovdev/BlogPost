from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect

from article.form import CommentForm
from article.models import Article, Tag, Category, Author, Comment
from django.contrib import messages


def article_list_page(request):
    object_list = Article.objects.order_by('-id')
    top_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        "object_list": object_list,
        "top_articles": top_articles,
        "categories": categories,
        "tags": tags,
    }
    return render(request, 'article/archive.html', ctx)


# def single_blog_page(request, slug):
#     article = get_object_or_404(Article, slug=slug)
#     object_list = Article.objects.order_by('-id')
#     next_post = Article.objects.filter(slug__gt=slug).first()
#     prev_post = Article.objects.filter(slug__lt=slug).last()
#     parent_id = request.POST.get('parent_id')
#     form = CommentForm()
#     if request.method == 'POST':
#         print(request.POST)
#         obj = CommentForm(request.POST, request.FILES)
#         if obj.is_valid():
#             obj = form.save(commit=False)
#             obj.article = article
#             obj.save()
#             messages.success(request, 'Your comment was successfully added!')
#             return redirect('.')
#     author = request.GET.get('authors')
#     comments = Comment.objects.filter(article_id=article.id).order_by('-id')
#     print(comments)
#     ctx = {
#         "object": article,
#         "object_list": object_list,
#         "next_post": next_post,
#         "prev_post": prev_post,
#         "form": form,
#         "author": author,
#         "comments": comments,
#     }
#     return render(request, 'article/single-blog.html', ctx)


def single_blog_page(request, slug, *args, **kwargs):
    form = CommentForm()
    article = get_object_or_404(Article, slug=slug)
    object_list = Article.objects.order_by('-id')[:3]
    tags = Tag.objects.order_by("-id")
    categories = Category.objects.order_by("-id")
    comments = Comment.objects.filter(article_id=article.id, top_level_comment_id__isnull=True)
    cid = request.GET.get('cid')
    if request.method == "POST":
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.parent_id = cid
            comment.save()
            messages.success(request, 'Comment sent successfully!')
            return redirect(f".#comments-{cid}")

    next = Article.objects.filter(pk__gt=article.pk).order_by('pk').first()
    previous = Article.objects.filter(pk__lt=article.pk).order_by('-pk').first()

    context = {
        'object': article,
        "object_list": object_list,
        'tags': tags,
        'categories': categories,
        'form': form,
        'next_post': next,
        'prev_post': previous,
        'comments': comments,
    }
    return render(request, 'article/single-blog.html', context)


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


