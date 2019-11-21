from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

<<<<<<< HEAD
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# from django.shortcuts import render
# from .models import Article
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from django.http import Http404
# from .serializers import ArticleSerializer
# from rest_framework import mixins
# from rest_framework import generics


# # def home(request):
# # 	articles = Article.objects.all()
# # 	return render(request, 'blog/home.html', {'articles':articles})
# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# # -------------------
# class ArticleView(APIView):
# #     def get_object(self, pk):
# #         try:
# #             return Article.objects.get(pk=pk)
# #         except Article.DoesNotExist:
# #             raise Http404

# #     def get(self, request, pk, format=None):
# #         article = self.get_object(pk)
# #         serializer = ArticleSerializer(article)
# #         return Response(serializer.data)

# #     def put(self, request, pk, format=None):
# #         article = self.get_object(pk)
# #         serializer = ArticleSerializer(article, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk, format=None):
# #         article = self.get_object(pk)
# #         article.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
# # ----------------------
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})

#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def post(self, request):
#     #     # article = request.data.get('article')
#     #     # Create an article from the above data
#     #     serializer = ArticleSerializer(data=request.data)
#     #     if serializer.is_valid(raise_exception=True):
#     #         article_saved = serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
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
>>>>>>> 08846a0d3c99fa3c7883a2a08e3c5e6a26f93560
