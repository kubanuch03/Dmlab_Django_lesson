from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'biography',
    )
    search_fields = (
        'full_name',
    )
