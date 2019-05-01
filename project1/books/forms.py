from django import forms
from .models import Book
from django.forms import ModelForm


class SearchForm(forms.Form):
    search = forms.CharField(label="поиск", max_length=200)


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name',)
