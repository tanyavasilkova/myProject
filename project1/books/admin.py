from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "date_of_entry", "change_date"]
    search_fields = ['name']

    class Meta:
        model = models.Book


admin.site.register(models.Book, BookAdmin)