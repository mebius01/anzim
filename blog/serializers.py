from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    article = serializers.CharField()
    status = serializers.CharField()
    tags = TagListSerializerField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)