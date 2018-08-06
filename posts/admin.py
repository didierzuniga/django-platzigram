from django.contrib import admin
from django.contrib.auth.models import User

# Models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('pk', 'title')
	list_display_links = ('pk', 'title')
	search_fields = ('pk', 'title')
	list_filter = ('created', 'modified')