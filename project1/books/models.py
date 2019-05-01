from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse_lazy


class Book(models.Model):
    name = models.CharField("Наименование", max_length=100)
    null = True
    blank = False

    image = models.ImageField("Обложка", upload_to="images")

    price = models.DecimalField(
        "Стоимость",
        max_digits=6,
        decimal_places=2
    )

    author = models.ManyToManyField(
        "catalog.Author",
        verbose_name="Авторы",
        related_name="books"
    )

    serie = models.ForeignKey(
        "catalog.Serie",
        verbose_name="Серия",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    genre = models.ManyToManyField(
        "catalog.Genre",
        verbose_name="Жанры",
        related_name="books"
    )

    year = models.IntegerField(
        "Год издания",
        null=True
    )

    numb_pages = models.IntegerField(
        "Количество страниц",
    )

    binding = models.ManyToManyField(
        "catalog.Binding",
        verbose_name="Переплет",
        related_name="books",
    )

    format = models.CharField(
        "Формат",
        max_length=30
    )

    isbn = models.CharField(
        "ISBN",
        max_length=20
    )

    age_restrictions = models.CharField(
        "Возрастные ограничения",
        max_length=20
    )

    publish = models.ForeignKey(
        "catalog.Publish",
        verbose_name="Издательство",
        related_name="books",
        on_delete=models.PROTECT

    )

    books_in_stock = models.IntegerField(
        "Наличие книг",
    )

    active = models.BooleanField(
        "Доступно для заказа",
        default=True
    )

    rating = models.FloatField(
        "Рейтинг",
        default=0
    )

    date_of_entry = models.DateTimeField(
        "Дата создания",
        auto_now=False,
        auto_now_add=True
    )
    change_date = models.DateTimeField(
        "Дата последнего изменения карточки",
        auto_now=True,
        auto_now_add=False
    )


    def get_absolute_url(self):
        return reverse_lazy("book_list_view")

    def __srt__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"





