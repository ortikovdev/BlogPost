from django.contrib import admin
from .models import (
    Category,
    Tag,
    Article,
    SubArticle,
    Comment,
)
from django.contrib.admin.options import InlineModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Tag)
class TagAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('name', )


class SubArticleInlineAdmin(admin.StackedInline):
    model = SubArticle
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleInlineAdmin, )
    list_display = ('id', 'category', 'title', )
    readonly_fields = ('slug', 'created_date', 'modified_date', )
    search_fields = ('title', )
    list_filter = ("category", "tags")
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'get_image', 'created_date')
    search_fields = ('name', 'article__title')
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
    # filter_horizontal = ('')