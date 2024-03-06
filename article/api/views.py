from django.shortcuts import get_object_or_404
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
def article_detail_page(request, pk):
    object_list = get_object_or_404(Article, id=pk)
    serializer = ArticleSerializer(object_list)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def article_create(request):
    print(request.data)
    # context = {
    #     'user_id': request.data.id
    # }
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        obj = get_object_or_404(Article, slug=serializer.data.get('slug'))
        success_serializer = ArticleSerializer(obj)
        return Response(success_serializer.data, status=status.HTTP_201_CREATED)
    data = {
        'errors': serializer.errors,
        'message': 'Something went wrong!'
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def top_comment_count(request):
    top_articles = Article.objects.annotate(comment_count=Count('comments')).order_by('-id')
    serializer = ArticleSerializer(top_articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH'])
def category_list_page(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tag_list_page(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


