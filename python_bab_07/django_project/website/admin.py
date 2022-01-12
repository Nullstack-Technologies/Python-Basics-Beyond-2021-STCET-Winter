from django.contrib import admin

from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date']
    list_filter = ['birth_date']
    search_fields = ['name']

