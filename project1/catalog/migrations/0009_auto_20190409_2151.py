# Generated by Django 2.2 on 2019-04-09 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_binding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
    ]