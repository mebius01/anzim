"""grpiglet URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='blog_detail'),
    path('api/list_all/', ArticleList.as_view(), name='api_home'),
    path('api/<int:pk>/', ArticleDetail.as_view(), name='id_post'),

]
