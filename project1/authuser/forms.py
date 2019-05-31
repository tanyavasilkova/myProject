from django import forms
from .models import AuthUser


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'avatar',
            'phone',
            'country',
            'city',
            'index',
            'address1',
            'address2',
            'info'
        )
        widgets = {
            'groups': forms.HiddenInput(),
            }


