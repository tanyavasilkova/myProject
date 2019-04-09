from django.contrib import admin
from . models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class SerieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


class PublishAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class BindingAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



admin.site.register(Author, AuthorAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Publish, PublishAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Binding, BindingAdmin)
