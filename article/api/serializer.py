from rest_framework import serializers
from article.models import Article, Category, Tag, Author
from django.utils.text import slugify


class ArticleSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def validate(self, attrs):
        if self.Meta.model.objects.filter(title=attrs['title']).exists():
            pass

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
