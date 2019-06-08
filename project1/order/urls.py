from django.urls import path
from .views import OrderCheckoutView, OrderDetailView, OrderListView


urlpatterns = [
    path('', OrderCheckoutView.as_view(), name='order-create'),
    path('<int:pk>', OrderDetailView.as_view(), name='order_detail_view'),
    path('list/', OrderListView.as_view(), name='order_list_view'),
]