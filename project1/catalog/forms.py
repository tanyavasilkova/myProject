from django import forms
from .models import Author, Serie, Publish, Genre, Binding
from django.forms import ModelForm


class SearchForm(forms.Form):
    search = forms.CharField(label="поиск", max_length=200)


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class SerieCreateForm(ModelForm):
    class Meta:
        model = Serie
        fields = ('name', 'description')


class PublishCreateForm(ModelForm):
    class Meta:
        model = Publish
        fields = ('name', 'description')


class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)


class BindingCreateForm(ModelForm):
    class Meta:
        model = Binding
        fields = ('name',)


