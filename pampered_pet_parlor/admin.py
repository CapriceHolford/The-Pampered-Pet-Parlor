from django.contrib import admin
from .models import BlogPost
from .models import Booking

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Show the author in the admin list view
    list_filter = ('author', 'created_at')  # Filter by author and date
    search_fields = ('title', 'content', 'author__username')  # Search by title, content, and author's username

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'service')