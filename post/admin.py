from django.contrib import admin
from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content', 'created_at']
    list_display = ['author', 'title', 'created_at']
    list_display_links = ['author', 'title']
    list_filter = ['author']
    search_fields = ['title', 'author__email', "author__username"]

    readonly_fields = ['created_at']

