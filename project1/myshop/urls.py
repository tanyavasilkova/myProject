"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import include, path

from catalog.views import *




urlpatterns = [
    path('admin/', admin.site.urls),

    path('catalog/author/<int:pk>', AuthorDetail.as_view(), name='author_detail_view'),
    path('catalog/serie/<int:pk>', SerieDetail.as_view(), name='serie_detail_view'),
    path('catalog/publish/<int:pk>', PublishDetail.as_view(), name='publish_detail_view'),
    path('catalog/genre/<int:pk>', GenreDetail.as_view(), name='genre_detail_view'),
    path('catalog/binding/<int:pk>', BindingDetail.as_view(), name='binding_detail_view'),

    path('catalog/author', AuthorList.as_view(), name='author_list_view'),
    path('catalog/serie', SerieList.as_view(), name='serie_list_view'),
    path('catalog/publish', PublishList.as_view(), name='publish_list_view'),
    path('catalog/genre', GenreList.as_view(), name='genre_list_view'),
    path('catalog/binding', BindingList.as_view(), name='binding_list_view'),

    path('allcatalogs', AllCatalogs.as_view()),

    #path('catalog/serie/create', SerieCreateView.as_view()),

    path('', include('main.urls')),
    path('contacts/', include('contacts.urls')),
    path('books/', include('books.urls')),

]
