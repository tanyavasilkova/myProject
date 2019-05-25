from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .forms import SearchForm, AuthorCreateForm, SerieCreateForm, PublishCreateForm, GenreCreateForm, BindingCreateForm
from  django.contrib.auth.mixins import PermissionRequiredMixin


class Search(ListView):

    def get_queryset(self):
        gs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if search != 0:
            return gs.filter(name__startswith=search)
        return gs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm()
        return context


class AuthorDetail(DetailView):
    model = Author


class AuthorList(Search):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'catalog_form.html'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'catalog_form.html'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list_view')
    template_name = 'catalog_confirm_delete.html'


class SerieDetail(DetailView):
    model = Serie


class SerieList(PermissionRequiredMixin, Search):
    #permission_required = ''
    model = Serie



class SerieCreateView(CreateView):
    model = Serie
    form_class = SerieCreateForm
    template_name = 'catalog_form.html'

    def get_success_url(self):
        return reverse_lazy('serie_detail_view', kwargs={'pk': self.object.pk})




class SerieUpdateView(UpdateView):
    model = Serie
    form_class = SerieCreateForm
    template_name = 'catalog_form.html'


class SerieDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'contenttypes.delete_contenttypes'
    model = Serie
    success_url = reverse_lazy('serie_list_view')
    template_name = 'catalog_confirm_delete.html'


class PublishDetail(DetailView):
    model = Publish


class PublishList(Search):
    model = Publish


class PublishCreateView(CreateView):
    model = Publish
    form_class = PublishCreateForm
    template_name = 'catalog_form.html'




class PublishUpdateView(UpdateView):
    model = Publish
    form_class = PublishCreateForm
    template_name = 'catalog_form.html'


class PublishDeleteView(DeleteView):
    model = Publish
    success_url = reverse_lazy('publish_list_view')
    template_name = 'catalog_confirm_delete.html'





class GenreDetail(DetailView):
    model = Genre


class GenreList(Search):
    model = Genre


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'catalog_form.html'

class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'catalog_form.html'


class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy('genre_list_view')
    template_name = 'catalog_confirm_delete.html'


class BindingDetail(DetailView):
    model = Binding


class BindingList(Search):
    model = Binding


class BindingCreateView(CreateView):
    model = Binding
    form_class = BindingCreateForm
    template_name = 'catalog_form.html'


class BindingUpdateView(UpdateView):
    model = Binding
    form_class = BindingCreateForm      #(могу ли здесь написать BindingCreateForm,
    template_name = 'catalog_form.html'


class BindingDeleteView(DeleteView):
    model = Binding
    success_url = reverse_lazy('binding_list_view')
    template_name = 'catalog_confirm_delete.html'



class AllCatalogs(TemplateView):
    template_name = "catalog/AllCatalogs.html"


def index(request):
    return HttpResponse("Справочники")