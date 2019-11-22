from rest_framework import serializers
from .models import Article
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Article
        fields = ['id', 'slug', 'title', 'article', 'status', 'tags']