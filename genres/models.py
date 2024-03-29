from django.db import models
from common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
