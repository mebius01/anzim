from django.contrib import admin
from .models import Article, Author
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'publish', 'status', 'get_absolute_url',)
	prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'salutation')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)