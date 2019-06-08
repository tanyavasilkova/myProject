from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import AuthUser
from .forms import AuthUserForm, AuthUserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class AuthUserCreate(CreateView):
    model = AuthUser
    form_class = AuthUserForm
    template_name = 'authuser/authuser_create.html'

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return reverse_lazy('login')


class AuthUserDetail(DetailView):
    model = AuthUser
    template_name = 'authuser/authuser_detail.html'
    def get_object(self, queryset=None):
        return self.request.user


class AuthUserUpdate(LoginRequiredMixin, UpdateView):
    model = AuthUser
    form_class = AuthUserUpdateForm
    template_name = 'update_form.html'

    def get_object(self):
        return self.request.user.authuser

    def get_success_url(self):

        return reverse_lazy('auth_detail_view')


    #dispatch = login_required(UpdateView.dispatch)




#class AuthUserDelete(DeleteView):
#    model = AuthUser
#    success_url = reverse_lazy('book_list_view')
#    template_name = 'catalog_confirm_delete.html'


