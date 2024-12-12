from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Show the author in the admin list view
    list_filter = ('author', 'created_at')  # Filter by author and date
    search_fields = ('title', 'content', 'author__username')  # Search by title, content, and author's username
