# from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    content = RichTextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SubArticle(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    header_content = RichTextField(null=True, blank=True)
    footer_content = RichTextField(null=True, blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)