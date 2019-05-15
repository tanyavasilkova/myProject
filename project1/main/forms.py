from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label="поиск", max_length=200)


