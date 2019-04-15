from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.views.generic import DetailView


class AuthorDetail(DetailView):
    model = Author


class SerieDetail(DetailView):
    model = Serie
    template_name = '11.html'


class PublishDetail(DetailView):
    model = Publish


class GenreDetail(DetailView):
    model = Genre


class BindingDetail(DetailView):
    model = Binding


def index(request):
    return HttpResponse("Справочники")