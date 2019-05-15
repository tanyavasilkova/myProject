from django.urls import path
from catalog.views import *


urlpatterns = [

    path('allcatalogs/', AllCatalogs.as_view(), name='allcatalogs_list_view'),

    path('author/', AuthorList.as_view(), name='author_list_view'),
    path('serie/', SerieList.as_view(), name='serie_list_view'),
    path('publish/', PublishList.as_view(), name='publish_list_view'),
    path('genre/', GenreList.as_view(), name='genre_list_view'),
    path('binding/', BindingList.as_view(), name='binding_list_view'),

    path('author/<int:pk>', AuthorDetail.as_view(), name='author_detail_view'),
    path('serie/<int:pk>', SerieDetail.as_view(), name='serie_detail_view'),
    path('publish/<int:pk>', PublishDetail.as_view(), name='publish_detail_view'),
    path('genre/<int:pk>', GenreDetail.as_view(), name='genre_detail_view'),
    path('binding/<int:pk>', BindingDetail.as_view(), name='binding_detail_view'),

    path('author/create/', AuthorCreateView.as_view(), name='author_create_view'),
    path('serie/create/', SerieCreateView.as_view(), name='serie_create_view'),
    path('publish/create/', PublishCreateView.as_view(), name='publish_create_view'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create_view'),
    path('binding/create/', BindingCreateView.as_view(), name='binding_create_view'),

    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author_update_view'),
    path('serie/update/<int:pk>', SerieUpdateView.as_view(), name='serie_update_view'),
    path('publish/update/<int:pk>', PublishUpdateView.as_view(), name='publish_update_view'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre_update_view'),
    path('binding/update/<int:pk>', BindingUpdateView.as_view(), name='binding_update_view'),

    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete_view'),
    path('serie/delete/<int:pk>', SerieDeleteView.as_view(), name='serie_delete_view'),
    path('publish/delete/<int:pk>', PublishDeleteView.as_view(), name='publish_delete_view'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre_delete_view'),
    path('binding/delete/<int:pk>', BindingDeleteView.as_view(), name='binding_delete_view'),

]