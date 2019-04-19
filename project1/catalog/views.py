from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView, ListView


class AuthorDetail(DetailView):
    model = Author

class AuthorList(ListView):
    model = Author


class SerieDetail(DetailView):
    model = Serie
    template_name = '11.html'


class SerieList(ListView):
    model = Serie


class PublishDetail(DetailView):
    model = Publish

class PublishList(ListView):
    model = Publish


class GenreDetail(DetailView):
    model = Genre

class GenreList(ListView):
    model = Genre


class BindingDetail(DetailView):
    model = Binding

class BindingList(ListView):
    model = Binding





def index(request):
    return HttpResponse("Справочники")