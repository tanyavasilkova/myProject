# Generated by Django 2.2 on 2019-04-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190408_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='publish',
            old_name='name_publish',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='serie',
            old_name='series',
            new_name='name',
        ),
    ]
