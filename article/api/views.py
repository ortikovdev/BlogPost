from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Q
from article.api.serializer import ArticleSerializer, CategorySerializer, TagSerializer
from article.models import (
    Article,
    Category,
    Tag,
)


@api_view(['GET'])
def article_list_page(request):
    object_list = Article.objects.all()
    serializer = ArticleSerializer(object_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_comment_count(request):
    top_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-id')
    serializer = ArticleSerializer(top_articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list_page(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tag_list_page(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
