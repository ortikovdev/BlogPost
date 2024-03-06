from rest_framework import serializers
from article.models import Article, Content,Category, Tag, Author
from django.utils.text import slugify


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'content', 'is_quote']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'image', 'email', 'description', 'created_date']


class ArticleSerializer(serializers.ModelSerializer):
    # content = ContentSerializer(many=True)
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'slug', 'image', 'tags', 'category', 'created_date', 'modified_date']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def validate(self, attrs):
        if self.Meta.model.objects.filter(title=attrs['title']).exists():
            pass


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'slug', 'image', 'tags', 'category', 'created_date', 'modified_date']