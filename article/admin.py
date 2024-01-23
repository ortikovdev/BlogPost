from django.contrib import admin
from .models import (
    Category,
    Tag,
    Article,
    SubArticle,
    Comment,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('name', )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', )
    # readonly_fields = ('created_date', 'modified_date', )
    search_fields = ('title', )
    list_filter = ("category", "tags")
    # date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )
