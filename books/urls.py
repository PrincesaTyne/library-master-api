from django.urls import path
from books.views import BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
  path('', BookListView.as_view(), name='book-list'),
  path('<str:id>', BookDetailView.as_view(), name='book-detail'),
]
