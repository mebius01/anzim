from django.shortcuts import render
from .models import Article
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer


# def home(request):
# 	articles = Article.objects.all()
# 	return render(request, 'blog/home.html', {'articles':articles})
# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    # def post(self, request):
    #     article = request.data.get('article')
    #     # Create an article from the above data
    #     serializer = ArticleSerializer(data=article)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    # def put(self, request, slug):
    #     saved_article = get_object_or_404(Article.objects.all(), slug=slug)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({
    #         "success": "Article '{}' updated successfully".format(article_saved.title)
    #     })