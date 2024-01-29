# from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='authors')
    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contents')
    content = RichTextField(null=True, blank=True)
    is_quote = models.BooleanField(default=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    message = models.TextField()
    email = models.EmailField(null=True, blank=True, max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" width="50" hight="50"></a>')
        return '-'



def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title+ "-" +timezone.now().strftime('%Y/%m/%d'))


pre_save.connect(article_pre_save, sender=Article)