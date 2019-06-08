from django.views.generic import  UpdateView, DetailView, ListView, DeleteView
from books.models import  Book
from order.models import  Order
from .models import Cart, BookInCart
from .forms import AddBookForm
from order.models import OrderStatus
from order.forms import CheckoutOrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


new_order_status = OrderStatus.objects.get(pk=1)


class AddBookToCart(UpdateView):
    model = BookInCart
    form_class = AddBookForm
    template_name = 'cart/add_book.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')

        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user

        cart, created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        self.request.session['cart_id']=cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            book_in_cart.quantity += 1
            book_in_cart.save()
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = self.kwargs.get('pk')
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', '/')


class CartDetail(DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, cart_created = Cart.objects.get_or_create(pk=cart_id, defaults={'user': user})
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckoutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = new_order_status
        context['form'] = checkout_form
        return context


class CartDelete(DeleteView):
    model = BookInCart
    template_name = 'cart/cart_delete.html'
    success_url = reverse_lazy("cart_detail_view")




class CartOrderList(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    # login_url = '/ /login'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        current_user = self.request.user
        return qs.filter(user=current_user)


class CartOrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'catalog_confirm_delete.html'
    success_url = reverse_lazy("cart_list_view")




