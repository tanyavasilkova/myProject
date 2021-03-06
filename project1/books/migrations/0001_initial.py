# Generated by Django 2.2 on 2019-06-06 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Обложка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
                ('year', models.IntegerField(null=True, verbose_name='Год издания')),
                ('numb_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('format', models.CharField(max_length=30, verbose_name='Формат')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN')),
                ('age_restrictions', models.CharField(max_length=20, verbose_name='Возрастные ограничения')),
                ('books_in_stock', models.IntegerField(verbose_name='Наличие книг')),
                ('active', models.BooleanField(default=True, verbose_name='Доступно для заказа')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('date_of_entry', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения карточки')),
                ('author', models.ManyToManyField(related_name='books', to='catalog.Author', verbose_name='Авторы')),
                ('binding', models.ManyToManyField(related_name='books', to='catalog.Binding', verbose_name='Переплет')),
                ('genre', models.ManyToManyField(related_name='books', to='catalog.Genre', verbose_name='Жанры')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='catalog.Publish', verbose_name='Издательство')),
                ('serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.Serie', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
