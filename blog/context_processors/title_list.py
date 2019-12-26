from blog.models import Article
def title_list(request):
	return {'title_list': Article.objects.all().order_by('-publish')}

def tag_list(request):
	return {'tag_list': Article.tags.most_common()}
