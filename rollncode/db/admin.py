from django.contrib import admin
from . import models


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    list_filter = ['gender']
    search_fields = ['surname']

    class Meta:
        model = models.Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn_code']
    list_filter = ['genre']
    search_fields = ['title', 'isbn_code']

    class Meta:
        model = models.Books


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Books, BookAdmin)
