from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status', 'get_absolute_url',)
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)