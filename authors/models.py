from django.db import models
from common.models import BaseModel


class Author(BaseModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
