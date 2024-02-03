from django.contrib import admin
from .models import (
    Category,
    Tag,
    Article,
    Content,
    Comment,
    Author,
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


class ContentInlineAdmin(admin.StackedInline):
    model = Content
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ContentInlineAdmin, )
    list_display = ('id', 'category', 'title', )
    readonly_fields = ('slug', 'created_date', 'modified_date', )
    search_fields = ('title', )
    list_filter = ("category", "tags")
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'message', 'name', 'get_image', 'created_date', 'top_level_comment_id')
    search_fields = ('name', 'article__title')
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
    # filter_horizontal = ('')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'created_date')
    search_fields = ('name', 'article__title')
    readonly_fields = ('created_date',)
    date_hierarchy = 'created_date'
