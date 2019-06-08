from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from .models import Order
from .forms import CheckoutOrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import Cart, BookInCart


class OrderCheckoutView(CreateView):
    model = Order
    template_name = 'cart/cart_detail.html'
    form_class = CheckoutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('main_view')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'

    def get_object(self, queryset=None):
        return self.request.user


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckoutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        context['form'] = checkout_form
        return context


class OrderListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    # login_url = '/ /login'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        current_user = self.request.user
        return qs.filter(user=current_user)

