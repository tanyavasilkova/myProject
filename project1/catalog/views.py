from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView
from .forms import SearchForm, AuthorCreateForm, SerieCreateForm, PublishCreateForm, GenreCreateForm, BindingCreateForm, SerieUpdateForm, AuthorUpdateForm, PublishUpdateForm, GenreUpdateForm, BindingUpdateForm

class Search(ListView):

    def get_queryset(self):
        gs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if search != 0:
            return gs.filter(name__startswith=search)
        return gs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f = SearchForm()
        context["form"] = f
        return context


class AuthorDetail(DetailView):
    model = Author


class AuthorList(Search):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorUpdateForm



class SerieDetail(DetailView):
    model = Serie
    template_name = '11.html'


class SerieList(Search):
    model = Serie


class SerieCreateView(CreateView):
    model = Serie
    form_class = SerieCreateForm


class SerieUpdateView(UpdateView):
    model = Serie
    form_class = SerieUpdateForm



class PublishDetail(DetailView):
    model = Publish


class PublishList(Search):
    model = Publish


class PublishCreateView(CreateView):
    model = Publish
    form_class = PublishCreateForm


class PublishUpdateView(UpdateView):
    model = Publish
    form_class = PublishUpdateForm


class GenreDetail(DetailView):
    model = Genre


class GenreList(Search):
    model = Genre


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreCreateForm


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreUpdateForm



class BindingDetail(DetailView):
    model = Binding


class BindingList(Search):
    model = Binding


class BindingCreateView(CreateView):
    model = Binding
    form_class = BindingCreateForm


class BindingUpdateView(UpdateView):
    model = Binding
    form_class = BindingUpdateForm #(могу ли здесь написать BindingCreateForm,
                                    #так тоже все работает# )



class AllCatalogs(TemplateView):
    template_name = "catalog/AllCatalogs.html"


def index(request):
    return HttpResponse("Справочники")