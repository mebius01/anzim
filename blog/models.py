from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):

	STATUS_CHOICES = (
		('personal', 'Personal'),
		('public', 'Public'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL',)# default=slugify('0'))
	article = RichTextUploadingField(blank=True, default='')
	# article = models.TextField(blank=True, default='')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='personal')
	tags = TaggableManager(help_text = "Список тегов, разделенных запятыми.", through=None, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return (self.slug)

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

# Create your models here.
