from django.db import models

# Create your models here.
class Book(models.Model):
    """Book represents a book in the library.

    A book has multiple attributes like name, author ISBN,
    pages and pulished date.
    """

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    pages = models.IntegerField()
    year = models.IntegerField()
