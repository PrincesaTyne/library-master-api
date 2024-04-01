from django.db import models
from common.models import BaseModel
from django.utils import timezone


class Borrowing(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} borrowed {self.book}'

    def save(self, *args, **kwargs):
        # Set the due_date to one week after the borrow_date
        if not self.due_date:
            if not self.borrow_date:
                self.borrow_date = timezone.now()
            self.due_date = self.borrow_date + timezone.timedelta(days=7)
        super().save(*args, **kwargs)
