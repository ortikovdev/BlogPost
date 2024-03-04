from django.urls import path
from .views import (
    article_list_page,
    category_list_page,
    tag_list_page,
    top_comment_count,
)

app_name = 'api'

urlpatterns = [
    path('article_list/', article_list_page, name='article-list'),
    path('category_list/', category_list_page, name='category-list'),
    path('tag_list/', tag_list_page, name='tag-list'),
    path('top_commented_articles/', top_comment_count, name='top-commented-articles'),
] # article/api/view_name/


