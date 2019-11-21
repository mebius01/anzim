from rest_framework import serializers
from .models import Article
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

<<<<<<< HEAD
class ArticleSerializer(serializers.ModelSerializer):
=======
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    article = serializers.CharField()
    status = serializers.CharField()
>>>>>>> 08846a0d3c99fa3c7883a2a08e3c5e6a26f93560
    tags = TagListSerializerField()
    class Meta:
        model = Article
        fields = ['id', 'title', 'article', 'status', 'tags']

<<<<<<< HEAD
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     article = serializers.CharField()
#     status = serializers.CharField()
#     tags = TagListSerializerField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.article = validated_data.get('article', instance.article)
#         instance.status = validated_data.get('status', instance.status)
#         instance.tags = validated_data.get('tags', instance.tags)
#         instance.save()
#         return instance


# from rest_framework import serializers
# from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     article = serializers.CharField()
#     status = serializers.CharField()
#     tags = TagListSerializerField()
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
=======
    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.article = validated_data.get('article', instance.article)
    #     instance.tags = validated_data.get('tags', instance.tags)
    #     instance.save()
    #     return instance
>>>>>>> 08846a0d3c99fa3c7883a2a08e3c5e6a26f93560
