from django.urls import path
from .views import AddBookToCart, CartDetail, CartOrderList, CartDelete, CartOrderDelete

urlpatterns = [
    path('<int:pk>', AddBookToCart.as_view(), name='cart'),
    path('detail/', CartDetail.as_view(), name="cart_detail_view"),
    path('delete/<int:pk>/', CartDelete.as_view(), name="cart_delete_view"),

    path('listorder/', CartOrderList.as_view(), name="cart_list_view"),
    path('deleteinorder/<int:pk>/', CartOrderDelete.as_view(), name="cart_order_delete_view"),
]
