from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug', 'user', 'checked']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['content']
    list_editable = ['title']
    
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

