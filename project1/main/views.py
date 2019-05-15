from django.http import HttpResponse
from django.views.generic import ListView
from books.models import Book
from django.db.models import Q
from .forms import SearchForm


class CardList(ListView):

    def get_queryset(self):
        gs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if search != 0:
            return gs.filter(Q(name__startswith=search)|Q(author__name__startswith=search)).distinct()
        return gs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm()
        return context


    model = Book
    template_name = 'main/main.html'



def index(request):
    return HttpResponse("<h2>Hello, world!<h2/>")

# Create your views here.
