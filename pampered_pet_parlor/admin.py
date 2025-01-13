from django.contrib import admin
from .models import BlogPost, Booking, ContactMessage

# Register BlogPost model with admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Display title, author, and creation date
    list_filter = ('author', 'created_at')  # Enable filtering by author and created date
    search_fields = ('title', 'content', 'author__username')  # Enable search by title, content, and author's username

# Register Booking model with admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin list view
    list_display = ('name', 'email', 'phone', 'date', 'time', 'service', 'breed', 'size', 'notes')

    # Add filters for fields like date and service
    list_filter = ('date', 'service')

    # Enable search functionality for key fields
    search_fields = ('name', 'email', 'phone', 'service')