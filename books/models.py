from django.db import models
from common.models import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=256)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('genres.Genre', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    number_of_copies = models.IntegerField(default=0)
    available_copies = models.IntegerField(default=0)
    published_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=256, null=True, blank=True)
    isbn = models.CharField(max_length=100, null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title
