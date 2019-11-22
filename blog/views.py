# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Author
from .serializers import ArticleSerializer
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListView(ListView):
    # model = Article
    context_object_name = 'articles'
    template_name = "blog/blog.html"
    # queryset = Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['author'] = Author.objects.all()
        return context
    queryset = get_context_data


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/blog_detail.html"


# class AuthorListView(ListView):
#     context_object_name = 'author'
#     queryset = Author.objects.all()
#     template_name = "blog/home.html"
