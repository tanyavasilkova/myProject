from django.http import HttpResponse


def index(request):
    return HttpResponse("Позвоните нам! Контакты: +375 29 000 00 00")

# Create your views here.
