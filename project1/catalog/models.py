from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):
    name = models.CharField("Автор", max_length=100)

    def get_absolute_url(self):
        return reverse_lazy("author_detail_view", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Serie(models.Model):
    null = True
    blank = True
    name = models.CharField("Серия", max_length=100)
    description = models.TextField("Описание")

    def get_absolute_url(self):
        return reverse_lazy("serie_list_view")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"
        permissions = ['catalog', 'can delete serie']


class Publish(models.Model):
    name = models.CharField("Издательство", max_length=30)
    description = models.CharField("Город", max_length=30)

    def get_absolute_url(self):
        return reverse_lazy('publish_detail_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=30)

    def get_absolute_url(self):
        return reverse_lazy('genre_detail_view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Binding(models.Model):
    name = models.CharField("Переплет", max_length=30)

    def get_absolute_url(self):
        return reverse_lazy('binding_list_view')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Переплет"
        verbose_name_plural = "Переплеты"

