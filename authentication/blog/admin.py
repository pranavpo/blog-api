# Register your models here.
from django.contrib import admin
from .models import Post

# Register Post model with the admin interface
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Columns to display in list view
    search_fields = ('title', 'content', 'author__username')  # Allow searching by title, content, and author username
    list_filter = ('author', 'created_at')  # Filter posts by author and created_at
    ordering = ('-created_at',)  # Order by creation date, most recent first
