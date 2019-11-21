from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    article = serializers.CharField()
    status = serializers.CharField()
    tags = TagListSerializerField()
    created = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.article = validated_data.get('article', instance.article)
    #     instance.tags = validated_data.get('tags', instance.tags)
    #     instance.save()
    #     return instance