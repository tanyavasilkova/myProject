from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import AuthUser
from .forms import AuthUserForm


class AuthUserCreate(CreateView):
    model = AuthUser
    form_class = AuthUserForm
    #template_name = 'catalog_form.html'

    #def get_success_url(self):
    #    return reverse_lazy('book_list_view')


class AuthUserDetail(DetailView):
    model = AuthUser


#class AuthUserUpdate(UpdateView):
#    model = AuthUser
#    form_class = BookCreateForm
#    template_name = 'catalog_form.html'


#class AuthUserDelete(DeleteView):
#    model = AuthUser
#    success_url = reverse_lazy('book_list_view')
#    template_name = 'catalog_confirm_delete.html'


