from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthUser(User, models.Model):
    user = models.OneToOneField(User, parent_link=True, related_name='authuser', on_delete=models.CASCADE)
    avatar = models.ImageField("Аватарка", upload_to="media", null=True, blank=True,)
    phone = models.CharField('Контактный телефон', help_text='+375*********', max_length=16)
    country = models.CharField('Страна', max_length=50, null=True, blank=True)
    city = models.CharField('Город', max_length=50, null=True, blank=True)
    index = models.IntegerField('Индекс', null=True, blank=True)
    address1 = models.CharField('Адрес1', max_length=200, null=True, blank=True)
    address2 = models.CharField('Адрес2', max_length=200, null=True, blank=True)
    info = models.CharField('Дополнительная информация', max_length=200, null=True, blank=True)








