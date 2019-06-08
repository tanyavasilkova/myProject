from django.urls import path
from .views import AuthUserCreate, AuthUserDetail, AuthUserUpdate


urlpatterns = [

    #path('', BookList.as_view(), name='book_list_view'),
    path('', AuthUserDetail.as_view(), name='auth_detail_view'),
    path('create/', AuthUserCreate.as_view(), name="auth_create_view"),
    path('update/', AuthUserUpdate.as_view(), name="auth_update_view"),
    #path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete_view'),
]


