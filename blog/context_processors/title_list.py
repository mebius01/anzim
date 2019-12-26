from blog.models import Article
def title_list(request):
	return {'title_list': Article.objects.all().order_by('-publish')}
