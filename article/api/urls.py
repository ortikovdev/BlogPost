from django.urls import path
from .views import (
    article_list_page,
    category_list_page,
    tag_list_page,
    top_comment_count,
    article_detail_page,
    article_create,
    article_delete,
)


app_name = 'api'

urlpatterns = [
    path('article_list/', article_list_page, name='list'),
    path('detail/<int:pk>/', article_detail_page, name='detail'),
    path('create/', article_create, name='create'),
    path('delete/<int:pk>/', article_delete, name='delete'),
    path('category_list/', category_list_page, name='category'),
    path('tag_list/', tag_list_page, name='tag'),
    path('top_commented_articles/', top_comment_count, name='top-commented-articles'),
] # article/api/view_name/


