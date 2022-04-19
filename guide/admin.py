from django.contrib import admin
from guide.models import Paper, Category

class PaperAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'published_date', )
    search_fields = ['title', 'content']

admin.site.register(Category)
admin.site.register(Paper, PaperAdmin)
