from django.urls import path
from .views import AddBookToCart, CartDetail

urlpatterns = [
    path('<int:pk>', AddBookToCart.as_view(), name='cart'),
    path('', CartDetail.as_view(), name="cart_detail_view"),
]
