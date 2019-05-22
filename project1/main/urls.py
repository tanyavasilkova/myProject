from django.urls import path

from .views import CardList

urlpatterns = [
    path('', CardList.as_view(), name='main_view'),

]