from django.urls import path
from genres.views import GenreListView, GenreDetailView

app_name = 'genres'

urlpatterns = [
  path('', GenreListView.as_view(), name='genre-list'),
  path('<str:id>', GenreDetailView.as_view(), name='genre-detail'),
]
