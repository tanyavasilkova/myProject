from django.urls import path

from books.views import BookList, BookDetail, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [

    path('', BookList.as_view(), name='book_list_view'),
    path('<int:pk>', BookDetail.as_view(), name='book_detail_view'),
    path('create/', BookCreateView.as_view(), name="book_create_view"),
    path('update/<int:pk>', BookUpdateView.as_view(), name="book_update_view"),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete_view'),
]
