from django.urls import path
from .views import (
    single_blog_page,
    article_list_page,
)

app_name = 'article'
urlpatterns = [
    path('list/', article_list_page, name='list'),
    path('detail/<slug:slug>/', single_blog_page, name='detail'),
]

