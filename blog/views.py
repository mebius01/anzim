from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from taggit.models import Tag
from django.db.models import Q

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Article.tags.most_common()
        return context

class ArticleListView(TagMixin, ListView):
    model = Article
    template_name = "blog/blog.html"
    paginate_by = 6
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(title__icontains = query) |
                Q(article__icontains = query))
        else:
            object_list = self.model.objects.all().order_by('-updated')
        return object_list

class TagView(TagMixin, ListView):
    model =Article
    template_name = 'blog/blog.html'
    def get_queryset(self):
        return Article.objects.filter(tags__slug = self.kwargs.get('slug'))

