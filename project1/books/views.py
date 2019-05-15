from django.shortcuts import render

# Create your views here.
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import SearchForm, BookCreateForm
from django.urls import reverse_lazy
from django.http import HttpResponse


class BookList(ListView):
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

    model = Book


class BookDetail(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'catalog_form.html'

    def get_success_url(self):
        return reverse_lazy('book_list_view')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'catalog_form.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list_view')
    template_name = 'catalog_confirm_delete.html'




def index(request):
    return HttpResponse("Книги")
