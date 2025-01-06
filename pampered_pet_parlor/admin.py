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
    list_display = ('name', 'email', 'date', 'time', 'service')  # Display booking details

# Register ContactMessage model with admin 
admin.site.register(ContactMessage)