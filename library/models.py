from django.db import models

# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    AuthorID = models.IntegerField()
    Publisher = models.CharField(max_length=30)
    PublishDate = models.CharField(max_length=30)
    Price = models.CharField(max_length=30)

class Author(models.Model):
    AuthorID = models.IntegerField()
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Country = models.CharField(max_length=30)
