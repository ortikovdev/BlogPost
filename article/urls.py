from django.urls import path, include
from .views import (
    single_blog_page,
    article_list_page,
    category_page,
)

app_name = 'article'
urlpatterns = [
    path('list/', article_list_page, name='list'),
    path('detail/<slug:slug>/', single_blog_page, name='detail'),
    path('category/', category_page, name='category'),
    path('api/', include('article.api.urls', namespace='api')),
]

