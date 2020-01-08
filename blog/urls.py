"""anzim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.contrib import admin
from django.urls import include, path
from blog.views import *
from django.views.generic import ListView, DetailView, TemplateView

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('about/', TemplateView.as_view(template_name = "blog/about.html"), name='about'),
    path('portfolio/', TemplateView.as_view(template_name = "blog/portfolio.html"), name='portfolio'),
    path('<slug:slug>/', DetailView.as_view(
        model = Article,
        template_name = "blog/blog_detail.html"), name='article_detail'),
    path('tags/<slug:slug>/', TagView.as_view(), name='tag_detail'),
    path('api/v1/articles/', ArticleList.as_view(), name='api_home'),
    path('api/v1/<int:pk>/', ArticleDetail.as_view(), name='id_post'),

]
