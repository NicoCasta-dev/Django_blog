from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    content = models.TextField()

    def __str__(self):
        return self.title + ' ' + self.author.first_name + ' ' + self.author.last_name

