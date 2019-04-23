from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from .forms import SearchForm

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


class SerieDetail(DetailView):
    model = Serie
    template_name = '11.html'


class SerieList(Search):
    model = Serie





#class SerieCreateView(CreateView):
#    model = Serie
#    fields = ['name']





class PublishDetail(DetailView):
    model = Publish

class PublishList(Search):
    model = Publish


class GenreDetail(DetailView):
    model = Genre

class GenreList(Search):
    model = Genre


class BindingDetail(DetailView):
    model = Binding

class BindingList(Search):
    model = Binding


class AllCatalogs(TemplateView):
    template_name = "catalog/AllCatalogs.html"




def index(request):
    return HttpResponse("Справочники")