# Generated by Django 2.2 on 2019-04-09 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190408_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
    ]
