from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'subject', 'created_date')
    search_fields = ['subject', 'message']

admin.site.register(Contact, ContactAdmin)
