from django.contrib import admin
from .models import Contact, Feedback


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    search_fields = ('name', 'email')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', )
    search_fields = ('name', 'position')
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date',)

