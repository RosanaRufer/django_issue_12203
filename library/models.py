from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True, through='AuthorsBooks')
    def __str__(self):
        return f"{self.name} by {', '.join([author.name for author in self.authors.all()])}"

class AuthorsBooks(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
