from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 10
    
# Register your models here.
