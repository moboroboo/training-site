from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'published_date', )
    search_fields = ['title', 'content']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)