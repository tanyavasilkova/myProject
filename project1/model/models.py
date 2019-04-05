
from django.db import models

class AuthorTable(models.Model):
    isbn = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class Serie(models.Model):
    isbn = models.CharField(max_length=30)
    series = models.IntegerField()

class  Publish(models.Model):
    isbn = models.CharField(max_length=30)
    name_publish = models.CharField(max_length=30)
    year_publish = models.IntegerField()

class Genre(models.Model):
    isbn = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

